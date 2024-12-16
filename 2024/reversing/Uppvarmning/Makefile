.PHONY: clean
all: dockerGrill handoutGrill
dockerGrill:
	sed "s/FAKEFLAG/GrillenGl0mdeUseAfterZ33/g" grill.c > docker/grill.c
	cd docker && gcc -o grill grill.c
handoutGrill:
	gcc -o grill grill.c
clean:
	rm -rf grill docker/grill
