/*
 * Generates flag and cookie values for challenge.c
 *
 * Note: Be careful so that there isn't any null (0x0) characters
 *       in the printed byte array.
 */

#include <stdio.h>
#include <string.h>

#define FLAG "cratectf{avlusning_med_ett_simpelt_knep}"
int cookie = 0x64415441; // "dATA"
int cookie2 = 0x6F747572; // "otur"

int
main(int argc, char *argv[])
{
	int i;
	char key[4];

        key[0] = (char)(cookie >>24 & 0xFF);
        key[1] = (char)(cookie >>16 & 0xFF);
        key[2] = (char)(cookie >>8 & 0xFF);
        key[3] = (char)(cookie & 0xFF);
        key[4] = '\0';

	printf("char flag[] = {\n");
	for (i = 0; i < strlen(FLAG); i++) {
		printf("0x%x, ", FLAG[i] ^ key[i % strlen(key)]);
		if (i && ((i % 8) == 0)) printf("\n");
	}
	printf("};\n\n");
	printf("#define COOKIE1 0x%X\n", cookie-cookie2);
	printf("#define COOKIE2 0x%X\n", cookie2);

	return 0;
}
