FLAG ?= Nature never uses prime numbers. But mathematicians do.
REPLACE_FLAG_PATTERN = \#REPLACE_FLAG\#

all:
	cp docker_template docker -r
	sed -i 's/${REPLACE_FLAG_PATTERN}/self._FLAG = "${FLAG}"/' docker/problemsolver.py 

clean:
	rm -rf docker
