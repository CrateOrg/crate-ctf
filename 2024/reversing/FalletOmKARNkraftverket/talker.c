#include <stdio.h>
#include <unistd.h>

int main(int argc, char ** argv) {
    setvbuf(stdout, NULL, _IONBF, 1024);

    while (1) {
        printf("Are you the one talking, or am I the one talking?\n");
        sleep(1);
    }

    return 0;
}
