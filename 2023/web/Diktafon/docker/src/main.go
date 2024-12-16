package main

import (
	"context"
	"crypto/sha256"
	"encoding/hex"
	"log/slog"
	"net/http"
	"os"
	"strings"
	"time"

	"challs.crate.nu/diktafon/components"
	"challs.crate.nu/diktafon/database"
	"challs.crate.nu/diktafon/files"
	"challs.crate.nu/diktafon/method"
	"challs.crate.nu/diktafon/sessions"

	"github.com/a-h/templ"
	"github.com/matthewhartstonge/argon2"
)

func main() {
	logFile, err := files.GetLogFile()
	if err != nil {
		panic(err)
	}
	slog.SetDefault(slog.New(slog.NewJSONHandler(logFile, nil)))

	for {
		err := database.Init()
		if err == nil {
			break
		}

		slog.Info("Connecting to database failed", "error", err)
		time.Sleep(time.Second)
	}

	{
		flagHash := sha256.Sum256([]byte(os.Getenv("FLAG")))
		adminPassword := hex.EncodeToString(flagHash[:])
		passwordHash, _ := argon.HashEncoded([]byte(adminPassword))
		_, err := database.CreateUser(context.Background(), "admin", passwordHash)
		if err != nil {
			panic(err)
		}
	}

	h := http.NewServeMux()
	routes(h)

	slog.Info("Server started", "addr", ":3000")
	http.ListenAndServe(":3000", sessions.New(WithLogger(h)))
}

func routes(h *http.ServeMux) {
	h.Handle("/", route(index))
	h.Handle("/register", method.Handler{Get: templ.Handler(components.Register()), Post: route(register)})
	h.Handle("/login", method.Handler{Get: templ.Handler(components.Login()), Post: route(login)})
	h.Handle("/logout", route(logout))
	h.Handle("/poem", route(poem))
}

func route(handler func(*slog.Logger, http.ResponseWriter, *http.Request) (templ.Component, error)) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		log := GetLogger(r.Context())
		if component, err := handler(log, w, r); err != nil {
			log.Error("Error handling request", "error", err)
			http.Error(w, http.StatusText(http.StatusInternalServerError), http.StatusInternalServerError)
		} else if component != nil {
			w.Header().Add("Content-Type", "text/html")
			component.Render(r.Context(), w)
		}
	})
}

func index(log *slog.Logger, w http.ResponseWriter, r *http.Request) (templ.Component, error) {
	username := sessions.LoggedInUser(r.Context())
	var f []string
	if username != "" {
		var err error
		f, err = files.ListPoems()
		if err != nil {
			return nil, err
		}
	}
	var flag string
	if sessions.LoggedInUser(r.Context()) == "admin" {
		flag = os.Getenv("FLAG")
		if flag == "" {
			http.Error(w, "Kunde inte hitta flaggan :( Kontakta en administratör", http.StatusInternalServerError)
			return nil, nil
		}
	}

	return components.Index(username, f, flag), nil
}

func poem(log *slog.Logger, w http.ResponseWriter, r *http.Request) (templ.Component, error) {
	if sessions.LoggedInUser(r.Context()) == "" {
		http.Error(w, "Du måste vara inloggad för att läsa dikter", http.StatusUnauthorized)
		return nil, nil
	}
	contents, err := files.GetPoem(r.FormValue("name"))
	if err != nil {
		return nil, err
	}
	return components.Poem(string(contents)), nil
}

var argon = argon2.DefaultConfig()

func register(log *slog.Logger, w http.ResponseWriter, r *http.Request) (templ.Component, error) {
	ctx := r.Context()
	username := strings.TrimSpace(r.FormValue("username"))
	password := r.FormValue("password")
	if len(username) < 4 {
		return components.RegisterForm([]string{"Användarnamnet måste vara minst 4 tecken"}, username), nil
	}
	hash, err := argon.HashEncoded([]byte(password))
	if err != nil {
		return nil, err
	}
	createdUser, err := database.CreateUser(ctx, username, hash)
	if err != nil {
		return nil, err
	}
	if !createdUser {
		return components.RegisterForm([]string{"Användarnamn upptaget"}, username), nil
	}
	log.Info("Account registered", "username", username)
	w.Header().Add("HX-Redirect", "/login")
	return nil, nil
}

func login(log *slog.Logger, w http.ResponseWriter, r *http.Request) (templ.Component, error) {
	ctx := r.Context()
	username := strings.TrimSpace(r.FormValue("username"))
	password := r.FormValue("password")
	hash, err := database.GetHash(ctx, username)
	if err != nil {
		return nil, err
	}
	if hash == nil {
		log.Info("Failed login attempt", "username", username)
		return components.LoginForm([]string{"Ogiltigt användarnamn"}, username), nil
	}
	ok, err := argon2.VerifyEncoded([]byte(password), hash)
	if err != nil {
		return nil, err
	}
	if !ok {
		log.Info("Failed login attempt", "username", username)
		return components.LoginForm([]string{"Felaktigt lösenord"}, username), nil
	}
	log.Info("Successful login", "username", username)
	if err := sessions.LogInAs(ctx, w, username); err != nil {
		return nil, err
	}
	w.Header().Add("HX-Redirect", "/")
	return nil, nil
}

func logout(log *slog.Logger, w http.ResponseWriter, r *http.Request) (templ.Component, error) {
	http.SetCookie(w, &http.Cookie{
		Name:   "login-session",
		MaxAge: -1,
	})
	w.Header().Add("HX-Redirect", "/")
	return nil, nil
}
