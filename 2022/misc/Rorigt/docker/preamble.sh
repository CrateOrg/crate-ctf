#!/bin/bash

function connection_error()
{
    echo "No connection to Crate CTF servers, exiting..."
    exit 1
}

echo Checking connection to Crate CTF servers, please wait...
ping -c 5 127.0.0.1 > /dev/null 2>&1 || connection_error

# If there's a lot of "^@" below, remove them using: cat script.sh | tr -d "\0" > script.sh

