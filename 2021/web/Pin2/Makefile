FLAG ?= cratectf{hashi_bashi_pumpkin_juice}
REPLACE_FLAG_PATTERN = \#REPLACE_FLAG\#

all:
	cp docker_template docker -r
	sed -i 's/${REPLACE_FLAG_PATTERN}/${FLAG}/' docker/src/CkEiORRyWcQZnJml9TFy_685407

clean:
	rm -rf docker

