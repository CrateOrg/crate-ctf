#include <stdio.h>

void print_flag()
{
    // "open" should be "r", this will cause a segmentation fault in getc() later since fptr = NULL
    FILE *fptr = fopen("/flag.txt", "open");

    char c;
    while ((c = getc(fptr)) != EOF)
    {
        putchar(c);
    }
    fflush(stdout);
    fclose(fptr);
}

int main()
{
    print_flag();
}
