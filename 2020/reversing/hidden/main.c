#include <stdio.h>
#include <string.h>

#define flag "REPLACE_FLAG"

int main(int argc, char* argv[]) {
	char buf[64];
	printf("Ge mig en flagga så kan jag kolla om den stämmer.\n");

	if(fgets(buf, 64, stdin) != NULL) {
		if(strncmp(buf, flag, strlen(flag)) == 0) {
			printf("Ja, den stämmer!\n");
		}
		else {
			printf("Nej, den stämmer inte!\n");
		}
	}

	return 0;
}
