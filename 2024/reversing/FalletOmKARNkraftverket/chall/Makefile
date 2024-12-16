obj-m += backdoor.o
backdoor-objs := main.o

CFLAGS_backdoor.o := -D_FORTIFY_SOURCE=0

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(shell pwd) modules

install:
	make -C /lib/modules/$(shell uname -r)/build M=$(shell pwd) modules_install

clean:
	@mv compile_commands.json compile_commands.json.bak 2>/dev/null || true
	make -C /lib/modules/$(shell uname -r)/build M=$(shell pwd) clean
	@mv compile_commands.json.bak compile_commands.json 2>/dev/null || true

talker: 
	gcc -o ./talker/talker ../talker.c
	cp ./talker/talker ..

.PHONY: talker
