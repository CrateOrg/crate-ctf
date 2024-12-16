#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

/*
Grammar:
S -> C '{' F '}' $
C -> 'cratectf'
F -> '[a-z_]' F | <empty>
*/

FILE* fp = NULL;
char current = '\0';
char* argv_debug;

int nextchar()
{
    while ((current = fgetc(fp)) == '\n')
    {}
    return current;
}

void terminate(const char* reason)
{
    fprintf(stderr, "%s\n", reason);
    exit(1);
}

void terminate_expected(const char* expected, char actual)
{
    fprintf(stderr, "Expected %s, found \"%c\"\n", expected, actual);
    exit(1);
}

void S();
void C();
void F(char c);

void S()
{
    C();
    if (current == '{')
    {
        F(nextchar());
        if (current == '}')
        {
            nextchar();
            if (current == -1)
            {
                return;
            }
            else
            {
                terminate_expected("EOF", current);
            }
        }
        else
        {
            terminate_expected("\"}\"", current);
        }
    }
    else
    {
        terminate_expected("\"{\"", current);
    }
}

void C()
{
    const char* ctf_name = "cratectf";
    for (int i = 0; i < strlen(ctf_name); i++)
    {
        if (current == ctf_name[i])
            nextchar();
        else
            terminate("Invalid CTF name");
    }
}

void F(char c)
{
    if (islower(current) || isdigit(current) || current == '_')
    {
        F(nextchar());
    }
    if (argv_debug)
    {
        // Trigger a segfault here to create a core dump
        fclose(fp); // Close the input file to avoid having its contents show up in the core dump
        printf("Debug: char = %s", current);
    }
}

int main(int argc, char** argv)
{
    if (argc < 2)
    {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        exit(1);
    }
    else if (argc >= 3)
        argv_debug = argv[2];

    fp = fopen(argv[1], "r");
    if (!fp)
        terminate("Cannot open file");
    nextchar();
    S();
    puts("The input file follows the flag format!");
}
