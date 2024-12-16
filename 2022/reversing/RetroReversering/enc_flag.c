#include <stdio.h>
#include <stdint.h>

uint8_t flag[] = {
    66, // C
    81, // R
    64, // A
    83, // T
    68, // E
    66, // C
    83, // T
    69, // F
    90, // {
    70, // G
    65, // B
    20, // _
    62, // 4
    68, // E
    85, // V
    68, // E
    81, // R
    92, // }
};
const int flag_len = 18;

int
main(int argc, char *argv[])
{
    int i = 0;
    uint8_t key=0xA3;

    printf("int flag[] = {\n");
    for (i = 0; i < flag_len; i++) {
        printf("    0x%x,\n", flag[i]^key);
        key++;
    }

    printf("};\n");

}
