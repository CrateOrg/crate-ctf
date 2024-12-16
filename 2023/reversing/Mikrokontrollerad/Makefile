CFLAGS = -mmcu=atmega328p

all:
	avr-gcc $(CFLAGS) challenge.c -o challenge
	avr-strip challenge

clean:
	rm -f challenge
