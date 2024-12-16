#include "stdio.h"
#include "stdlib.h"
#include "stdbool.h"
#include "string.h"

void print_flag() {
    FILE *fptr = fopen("flag.txt", "r");
    if (fptr == NULL) {
        printf("Could not open flag.txt... If you are connecting to the server, please contact an admin.");
        exit(0);
    }

    char c;
    while ((c = getc(fptr)) != EOF) {
        putchar(c);
    }
    fflush(stdout);
    fclose(fptr);
}

int main()
{
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);

    bool licenseValid = false;
    int flags = 1;

    while (true)
    {
        puts("* FLAG STORAGE SERVER v8.3.1 *");
        printf("Stored flags: %d\n", flags);
        if (licenseValid == true)
            puts("License: Standard");
        else
            puts("License: TRIAL (3 days left)");
        puts("");
        puts("Menu options:");
        puts("(1) Store flag");
        puts("(2) Retrieve flag");
        puts("(3) Delete flag");
        puts("(4) Enter license key");
        puts("(0) Quit");
        printf("Enter action: ");

        char action[3] = "";

        if (!fgets(action, sizeof(action), stdin))
            exit(0);
        switch (action[0])
        {
            case '0':
            {
                puts("Bye!");
                exit(0);
                break;
            }
            case '1':
            {
                puts("Sorry, that feature is only available for users with the GOLD subscription.");
                break;
            }
            case '2':
            {
                if (flags <= 0)
                {
                    puts("No flags available.");
                    break;
                }
                if (!licenseValid)
                {
                    puts("Sorry, that feature is not available in the trial version.");
                    break;
                }

                print_flag();

                break;
            }
            case '3':
            {
                flags = 0;
                puts("Flag deleted. Why would you do that??");

                break;
            }
            case '4':
            {
                // There are 160 keys that follow the format specified below, any of them will print the flag.
                // One valid key is: 90496-75839-01561-14361-92127
                char key[64] = "";

                printf("Enter license key: ");

                if (!fgets(key, sizeof(key) - 1, stdin))
                    break;

                key[strcspn(key, "\n")] = 0;

                if (strlen(key) == 29)
                {
                    int sum = 0;
                    bool correctChars = true;
                    for (int i = 0; i < strlen(key); i++)
                    {
                        sum += key[i];
                        if (i == 5 || i == 11 || i == 17 || i == 23)
                        {
                            if (key[i] != '-')
                                correctChars = false;
                        }
                        else
                        {
                            if (key[i] == '-')
                                correctChars = false;
                        }
                    }

                    if (correctChars)
                    {
                        if (sum == 0x5d1)
                        {
                            if (key[6] + key[7] + key[8] + key[9] + key[10] == 0x110)
                            {
                                if (key[0] == key[3] && key[3] == key[10] && key[10] == key[24])
                                {
                                    if (key[5] == '-')
                                    {
                                        if (key[0] == '9')
                                        {
                                            if (key[0] + key[1] + key[2] + key[3] + key[4] == 0x10c)
                                            {
                                                if (key[12] + key[13] + key[14] + key[15] + key[16] == 0xfd)
                                                {
                                                    if (key[13] == key[12] + 1)
                                                    {
                                                        if (key[14] == key[13] + 4)
                                                        {
                                                            if (strcmp(key + 24, "92127") == 0)
                                                            {
                                                                if (key[13] == key[16] && key[16] == key[18] && key[18] == key[26])
                                                                {
                                                                    if (key[4] == key[15] && key[15] == key[21])
                                                                    {
                                                                        if ((key[6] ^ key[7]) == 2)
                                                                        {
                                                                            if ((key[6] ^ key[10]) == 0xe)
                                                                            {
                                                                                if (key[19] == key[20] + 1)
                                                                                {
                                                                                    licenseValid = true;
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }

                if (licenseValid)
                {
                    puts("License key accepted! Thank you for choosing a genuine FLAG STORAGE (TM) product.");
                }
                else
                {
                    puts("Sorry, that is not a valid license key.");
                }

                break;
            }
        }
        puts("");
    }
}
