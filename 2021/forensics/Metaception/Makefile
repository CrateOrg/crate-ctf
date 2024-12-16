# apt packages: kid3-cli,mpg321,exiftool
# echo -n "cratectf{i_use_arch_btw} " | base64
FLAG:="Y3JhdGVjdGZ7aV91c2VfYXJjaF9idHd9IA=="

all:
	exiftool -PNGWarning="${FLAG}        " -z -o linux.png stallman.png
	mpg321 -w linux.wav Linus-linux.ogg.mp3
	kid3-cli -c "set artist 'Linus Torvalds'" linux.wav
	kid3-cli -c "set picture:./linux.png ''" linux.wav

clean:
	rm -f linux.wav
	rm -f linux.png
