.PHONY: clean
handout:
	cp -r docker dockerhandout
	echo "cratectf{redacted}" > dockerhandout/src/flag.txt
	zip -r handout.zip dockerhandout
	rm -r dockerhandout

clean:
	rm -rf handout.zip dockerhandout
