FLAG = "testctf{strings_mot_en_fil_bara}"

all:
	mkdir -p build
	cp main.c tempmain.c
	sed -i 's/REPLACE_FLAG/${FLAG}/' tempmain.c
	gcc -O2 tempmain.c -o chall
	rm tempmain.c
	mv chall build/

clean:
	rm -rf build
	rm -f tempmain.c
