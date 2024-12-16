main:
	gcc -fPIC -c main.c -o main.o
	gcc -shared -o pam_weird.so main.o -lpam -lgmp
	cp pam_weird.so /lib/security/
.PHONY: main
