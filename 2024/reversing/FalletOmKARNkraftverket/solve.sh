#! /bin/bash

sudo hping3 -S fok.challs.crate.nu -p 1288 -d 8 -E data.bin -c 1
sudo hping3 -S fok.challs.crate.nu -p 5134 -d 8 -E data.bin -c 1
sudo hping3 -S fok.challs.crate.nu -p 36112 -d 8 -E data.bin -c 1

nc fok.challs.crate.nu 50014
