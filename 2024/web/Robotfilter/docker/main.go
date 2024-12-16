package main

import (
	crand "crypto/rand"
	_ "embed"
	"encoding/base64"
	"encoding/binary"
	"errors"
	"fmt"
	"html/template"
	"log/slog"
	"math/rand/v2"
	"net/http"
	"os"
	"os/exec"
	"strconv"
	"strings"
	"sync"
)

var sessions []map[string]string
var sessionLock sync.Mutex

//go:embed index.html
var indexHTML []byte
var indexTemplate = template.Must(template.New("index.html").Parse(string(indexHTML)))

//go:embed mirror.png
var mirrorPNG []byte

// openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365 -nodes -subj '/CN=localhost' \
//     -addext "subjectAltName=$(BASE_DOMAIN=localhost go run . domains | sed 's/^/DNS:/' | paste -sd,)"

func s(i int) string {
	return strconv.Itoa(i)
}

type Rand struct {
	*rand.Rand
}

func (r Rand) sign(val int) int {
	if r.IntN(2) == 1 {
		return -val
	}
	return val
}

func (r Rand) between(from int, to int) int {
	return rand.IntN(to-from) + from
}

func ternary[T any](cond bool, then T, else_ T) T {
	if cond {
		return then
	} else {
		return else_
	}
}

var levelHostnames [90]string
var flagHostname string

func post(level int, w http.ResponseWriter, r *http.Request) {
	sessionID := r.FormValue("session")
	sessionLock.Lock()
	challenge, ok := sessions[level-1][sessionID]
	delete(sessions[level-1], sessionID)
	sessionLock.Unlock()
	if !ok {
		get(level, w, "Sessionen finns inte eller har gått ut. Försök igen")
		return
	}
	ans := r.FormValue("ans")
	if challenge != ans {
		get(level, w, "Fel svar, robot!")
		return
	}
	if level == len(levelHostnames) {
		http.Redirect(w, r, "https://"+flagHostname+"/", http.StatusSeeOther)
		return
	}
	http.Redirect(w, r, "https://"+levelHostnames[level] /* 0 and 1 index shenanigans, so this is the next level */ +"/", http.StatusSeeOther)
}

func get(level int, w http.ResponseWriter, errorMessage string) {
	var seed [16]byte
	if _, err := crand.Read(seed[:]); err != nil {
		slog.Error("Rand failed", "error", err)
		return
	}
	rand := Rand{rand.New(rand.NewPCG(binary.NativeEndian.Uint64(seed[:8]), binary.NativeEndian.Uint64(seed[8:])))}

	challengeRunes := make([]rune, 10+rand.IntN((level+9)/10))
	for i := range challengeRunes {
		all := []rune{
			'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
			'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
			'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
			',', '.', '/', '+', '-', '=', '!', '@', '#', '$',
			'%', '^', '&', '*', '(', ')', '_', '[', ']', '{', '}',
			'å', 'ä', 'ö', 'Å', 'Ä', 'Ö', 'ü', 'Ü', 'æ', 'Æ', 'ø', 'Ø',
		}
		avail := all[:min(len(all), 26+26+level*3)]
		challengeRunes[i] = avail[rand.IntN(len(avail))]
	}
	challenge := string(challengeRunes)
	polarBlur := rand.IntN(level+10) > 10
	args := [][]string{
		{"-size", "20x10"},
		{"xc:hsl(" + s(rand.IntN(360)) + "," + s(rand.IntN(256)) + "," + s(min(245, rand.IntN(200+level))) + ")"},
		{"("},
		{"+clone"},
		{"-fill", "white"},
		{"-attenuate", strconv.FormatFloat(max(min(rand.NormFloat64()/10+float64(level)/20, 1), 0), 'f', 4, 64)},
		{"+noise", "random"}, // TODO: this takes a while, maybe cache a few?
		{")", "-compose", "luminize", "-composite"},
		{"-resize", "1000x500"},
		{"-fill", "white"},
		{"-font", "./Caveat-VariableFont_wght.ttf"},
		{"-pointsize", s(rand.between(30, 100))},
		{"-gravity", "center"},
		{"-annotate", s(rand.sign(rand.IntN(level+5))) + "x" + s(rand.sign(rand.IntN(level+10))) + "+" + s(rand.sign(rand.IntN(200))) + "+" + s(rand.sign(rand.IntN(200))), challenge},
		ternary(polarBlur, []string{"-distort", "Polar", "0"}, []string{}),
		{"-blur", "6x" + s(rand.between(level*3/4, level+1))},
		ternary(polarBlur, []string{"-distort", "DePolar", "0"}, []string{}),
		{"-swirl", s(rand.sign(rand.between(level*10, level*20)))},
		{"png:-"},
	}
	var actualArgs []string
	for _, a := range args {
		actualArgs = append(actualArgs, a...)
	}
	cmd := exec.Command("magick", actualArgs...)
	output, err := cmd.Output()
	if err != nil {
		var ee *exec.ExitError
		var stderr []byte
		if errors.As(err, &ee) {
			stderr = ee.Stderr
		}
		slog.Error("Imagemagick failed", "error", err, "stderr", string(stderr))
		return
	}
	var sessionIDBytes [24]byte
	if _, err := crand.Read(sessionIDBytes[:]); err != nil {
		slog.Error("crypto/rand.Read failed", "error", err)
		return
	}
	sessionID := base64.StdEncoding.EncodeToString(sessionIDBytes[:])
	sessionLock.Lock()
	sessions[level-1][sessionID] = challenge
	sessionLock.Unlock()
	notSure := "inte " + strings.Repeat("helt ", max(0, level-2)) + "säkra"
	if level > 1 {
		notSure = "ännu " + notSure
	}
	indexTemplate.Execute(w, map[string]any{
		"imgAttr": template.HTMLAttr(
			`src="data:image/png;base64,` + base64.StdEncoding.EncodeToString(output) + `"`,
		),
		"sessionID":    sessionID,
		"notSure":      notSure,
		"errorMessage": errorMessage,
	})
}

func main() {
	baseDomain := os.Getenv("BASE_DOMAIN")
	if baseDomain == "" {
		slog.Error("Missing $BASE_DOMAIN environment variable")
		os.Exit(1)
	}

	certFile := os.Getenv("CERT_FILE")
	if certFile == "" {
		certFile = "./cert.pem"
	}
	keyFile := os.Getenv("KEY_FILE")
	if keyFile == "" {
		keyFile = "./key.pem"
	}

	sessions = make([]map[string]string, len(levelHostnames))
	for i := range sessions {
		sessions[i] = make(map[string]string)
	}
	{
		r := rand.New(rand.NewPCG(0xf01, 0xf01))
		for i := range levelHostnames {
			var name string
			for range 20 {
				name += string([]byte{byte('a' + r.IntN(26))})
			}
			levelHostnames[i] = fmt.Sprintf("level%d-%s.%s", i+1, name, baseDomain)
		}
		var name string
		for range 20 {
			name += string([]byte{byte('a' + r.IntN(26))})
		}
		flagHostname = fmt.Sprintf("flag-%s.%s", name, baseDomain)
	}
	if len(os.Args) > 1 && os.Args[1] == "domains" {
		fmt.Println(baseDomain)
		for _, hostname := range levelHostnames {
			fmt.Println(hostname)
		}
		fmt.Println(flagHostname)
		return
	}
	http.HandleFunc("/mirror.png", func(w http.ResponseWriter, r *http.Request) {
		w.Write(mirrorPNG)
	})
	http.Handle(fmt.Sprintf("GET %s/{$}", baseDomain), http.RedirectHandler("https://"+levelHostnames[0]+"/", http.StatusMovedPermanently))
	http.HandleFunc(fmt.Sprintf("GET %s/", flagHostname), func(w http.ResponseWriter, r *http.Request) {
		w.Header().Add("Content-Type", "text/plain; charset=utf-8")
		fmt.Fprintln(w, "cratectf{🤖😠🤖😠🤖}")
	})
	for i, domain := range levelHostnames {
		http.HandleFunc(fmt.Sprintf("POST %s/{$}", domain), func(w http.ResponseWriter, r *http.Request) {
			post(i+1, w, r)
		})
		http.HandleFunc(fmt.Sprintf("GET %s/{$}", domain), func(w http.ResponseWriter, r *http.Request) {
			get(i+1, w, "")
		})
	}
	slog.Info("Server starting", "addr", "https://"+baseDomain+"/")
	if err := http.ListenAndServeTLS(":443", certFile, keyFile, nil); err != nil {
		panic(err)
	}
}
