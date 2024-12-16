FLAG ?= cratectf{cmd_1nj3ct10ns_t0_th3_r35cu3}
REPLACE_FLAG_PATTERN = \#REPLACE_FLAG\#

all:
	cp docker_template docker -r
	sed -i 's/${REPLACE_FLAG_PATTERN}/${FLAG}/' docker/src/api.php

clean:
	rm -rf docker

