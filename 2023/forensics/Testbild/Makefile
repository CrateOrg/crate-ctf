# apt packages: qrencode, imagemagick
FLAG:=cratectf{kanske_trumfar_myrornas_krig}

all:
	qrencode -o flag.png "${FLAG}"
	convert flag.png -background white -extent 768x576 flag.png
	convert flag.png -channel RGB -negate flag.png
	convert input.png -fx R r.png
	convert input.png -fx G g.png
	convert input.png -fx B b.png
	convert b.png -fx '(int(u*255)&240)/255' b.png
	convert flag.png -fx '(int(u*255)&255)/(255*92)' flag.png
	convert -compose plus b.png flag.png -background black -layers flatten b.png
	convert r.png g.png b.png -set colorospace sRGB -combine challenge.png
	rm -f flag.png
	rm -f r.png
	rm -f g.png
	rm -f b.png

clean:
	rm -f challenge.png
