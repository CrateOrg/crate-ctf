FLAG ?= cratectf{sw1tchy_swoosh_got_sw1tch3d}
REPLACE_FLAG_PATTERN = \#REPLACE_FLAG\#

all:
	cp docker_template docker -r
	sed -i 's/${REPLACE_FLAG_PATTERN}/${FLAG}/' docker/romweb/config.php

clean:
	rm -rf docker

