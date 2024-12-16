#include <stdio.h>

#define NUMBPRIME 160000005

int main(int argc, char* argv[]) {
	int counter = 1;
	int current = 3;
	while(counter < (NUMBPRIME-1)) {
		int ok = 1;

		int test = current+1;
		while(1==1) {

			ok = 1;
			for(int i=test-1; i>1; --i) {
				if(test%i == 0) {
					ok = 0;
				}
			}

			if(ok == 1) {
				current = test;
				counter += 1;
				break;
			}

			++test;
		}
	}

	printf("2020ctf{%d}\n", current);

	return 0;
}
