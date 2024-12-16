FLAG ?= cratectf{th0se_t0ken_s3cre7ts_ar3_pr3c1ou5}
REPLACE_FLAG_PATTERN = \#REPLACE_FLAG\#

all:
	cp docker_template docker -r
	sed -i 's/${REPLACE_FLAG_PATTERN}/${FLAG}/' docker/manage.php 

clean:
	rm -rf docker

