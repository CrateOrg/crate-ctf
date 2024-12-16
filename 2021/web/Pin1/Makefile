FLAG ?= cratectf{easy_peasy_peaky_blinders}
REPLACE_FLAG_PATTERN = \#REPLACE_FLAG\#

all:
	cp docker_template docker -r
	sed -i 's/${REPLACE_FLAG_PATTERN}/${FLAG}/' docker/src/UyX6GGmgzWT52uKQcNfy

clean:
	rm -rf docker

