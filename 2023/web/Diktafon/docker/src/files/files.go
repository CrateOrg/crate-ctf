package files

import (
	"fmt"
	"io"
	"os"
	"path"
	"strings"
)

var baseLocation = "data"

func GetLogFile() (io.Writer, error) {
	return os.OpenFile(baseLocation+"/log.json", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0660)
}

func ListPoems() ([]string, error) {
	entries, err := os.ReadDir(baseLocation + "/poems")
	if err != nil {
		return nil, err
	}
	files := make([]string, len(entries))
	for i, entry := range entries {
		files[i] = entry.Name()
	}
	return files, nil
}

func GetPoem(name string) ([]byte, error) {
	return getFile(path.Join("poems", name))
}

func getFile(filepath string) ([]byte, error) {
	filepath = path.Join(baseLocation, filepath)
	if !strings.HasPrefix(filepath, baseLocation) {
		return nil, fmt.Errorf("File path `%v` is outside of the base location `%v`.", filepath, baseLocation)
	}
	return os.ReadFile(filepath)
}
