FLAG ?= cratectf{p1n_4pi_bru73_ach13vm3nt_unl0ck3d}
REPLACE_FLAG_PATTERN = \#REPLACE_FLAG\#

all:
	cp docker_template docker -r
	sed -i 's/${REPLACE_FLAG_PATTERN}/${FLAG}/' docker/src/api.php

clean:
	rm -rf docker

