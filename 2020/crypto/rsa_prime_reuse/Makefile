FLAG = "testctf{rsa_rs4_r5a_r54}"

all:
	mkdir -p build
	cp generate_cipher.py build/
	printf "SECRET = b\"%s\"\n" "$(FLAG)" > secret.py
	python3 generate_cipher.py 
	mv output.txt build/

clean:
	rm -rf build
	rm -f secret.py
	rm -f output.txt
	rm -rf __pycache__
