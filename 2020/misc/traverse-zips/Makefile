FLAG = "testctf{hurra_massor_av_zipfiler}"

all:
	rm -rf build
	mkdir -p build
	printf "$(FLAG)" > flagga.txt
	python3 create.py
	rm flagga.txt
	mv *.zip build/

clean:
	rm -rf build
	rm -f flagga.txt
	rm -rf __pycache__
	rm -rf *.zip
