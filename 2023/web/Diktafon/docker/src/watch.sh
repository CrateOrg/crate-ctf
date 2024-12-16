#!/bin/sh

find . -name '*.go' -or -name '*.templ' | entr -r sh -c 'go generate ./... && go run .'
