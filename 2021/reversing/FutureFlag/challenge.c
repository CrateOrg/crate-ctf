#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <sys/ptrace.h>

char flag[] = {
	0x07, 0x33, 0x35, 0x35, 0x01, 0x22, 0x20, 0x27,
	0x1f, 0x20, 0x22, 0x2d, 0x11, 0x32, 0x3a, 0x28,
	0x0a, 0x26, 0x0b, 0x2c, 0x01, 0x25, 0x0b, 0x24,
	0x10, 0x35, 0x0b, 0x32, 0x0d, 0x2c, 0x24, 0x24,
	0x08, 0x35, 0x0b, 0x2a, 0x0a, 0x24, 0x24, 0x3c
};

#define COOKIE1 0xF4CCDECF
#define COOKIE2 0x6F747572

void
decrypt_flag(int cookie)
{
	int i;
	char buf[256];
	char key[4];
       
	key[0] = (char)(cookie >>24 & 0xFF);
	key[1] = (char)(cookie >>16 & 0xFF);
	key[2] = (char)(cookie >>8 & 0xFF);
	key[3] = (char)(cookie & 0xFF);
	key[4] = '\0';

	memset(buf, 0, sizeof(buf));
	for (i = 0; i < strlen(flag); i++) {
		buf[i] = flag[i] ^ key[i % 4];
		printf("%c", buf[i]);
	}
}

int
main(int argc, char *argv[])
{
	int cookie = 0;
	time_t t1, t2;
	char buf[256];

	if (ptrace(PTRACE_TRACEME, 0, NULL, NULL) == 0) {
		cookie = COOKIE1;
	}

	if (ptrace(PTRACE_TRACEME, 0, NULL, NULL) == -1) {
		cookie += COOKIE2;
	}

	if (cookie != COOKIE1+COOKIE2) {
		return -1;
	}

	t1 = time(NULL);
	usleep(2);
	t2 = time(NULL);
	if (t1 < 1704063600) {
	  fprintf(stderr, "This program can't be run before 2024-01-01\n");
	  return -1;
	}
	if (t2 >= t1) {
	  fprintf(stderr, "The flag is probably in the past?\n");
	  return -1;
	}

	decrypt_flag(cookie);

	return 0;
}
