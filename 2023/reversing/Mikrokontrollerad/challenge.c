#define F_CPU 8000000UL
#ifndef __AVR_ATmega328P__
#define __AVR_ATmega328P__
#endif

#include <avr/io.h>

void UART_Tx(unsigned char data);
char message[] = {0x12, 0x3, 0x10, 0x5, 0x14, 0x12, 0x5, 0x17, 0xa, 0x1b, 0x4, 0x2, 0x5, 0x2e, 0x10, 0x1f,
                  0x2e, 0x30, 0x27, 0x23, 0x10, 0x16, 0x14, 0x2e, 0x1, 0x3, 0x1e, 0x16, 0x3, 0x10, 0x1c,
                  0x2e, 0x1f, 0x1e, 0x5, 0x19, 0x18, 0x1f, 0x16, 0x2e, 0x5, 0x1e, 0x2e, 0x2, 0x14, 0x14,
                  0x2e, 0x19, 0x14, 0x3, 0x14, 0xc};
volatile char xor_key = '\x42'; // Intentionally wrong, should be \x71 for a correct decode

int main(void)
{

    // Set UART0 to 9600 baud
    UBRR0 = F_CPU / (16L * 9600) - 1;
    // Set UART0 to asynchronous UART, 8 bits, no parity, 1 stop bit
    UCSR0C = 0b00000110;
    // Enable UART0
    UCSR0B |= (1 << TXEN0);

    for (int i = 0; i < sizeof(message) / sizeof(message[0]); i++)
    {
        UART_Tx(message[i] ^ xor_key);
    }
    UART_Tx('\n');

    return 0;
}

void UART_Tx(unsigned char data)
{
    // Wait for UART data register empty flag to be set
    while (!(UCSR0A & (1 << UDRE0)))
    {
    }
    UDR0 = data;
}
