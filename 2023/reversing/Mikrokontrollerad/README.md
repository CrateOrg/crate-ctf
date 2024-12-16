# Mikrokontrollerad

En AVR-binär som XOR-avkodar flaggan med fel nyckel och skriver ut den via USART. Med `file`, `objdump` och `strings` syns det att det är en ELF-binär för "Atmel AVR 8-bit", specifikt en ATmega328P. Att köra programmet med t.ex. [simavr](https://github.com/buserror/simavr) leder till att en sträng med skräptecken skrivs ut via serieporten (USART).

Om man använder t.ex. Ghidra och disassemblerar programmet hittas inte alltid main-funktionen. Med `avr-readelf -a challenge` kan man dock läsa ut `Entry point address: 0x0` (där alla AVR-processorer börjar exekvera kod). Att markera adress 0x0 som kod i Ghidra gör att main-funktionen upptäcks. Denna anropar en annan funktion i en loop. Den inre funktionen läser från 0x00c0 i "DAT_mem" och skriver till 0x00c6 i "DAT_mem":
```
008c std  Y+0x1,R24
009a ldd  R18,Y+0x1
008e ldi  R24,0xc0
008f ldi  R25,0x0
0090 movw Z,R25R24
0091 ld   R24,Z=>DAT_mem_00c0

[...]

0098 ldi  R24,0xc6
0099 ldi  R25,0x0
009a ldd  R18,Y+0x1
009b movw Z,R25R24
009c st   Z,R18=>DAT_mem_00c6
```
Från databladet för mikrokontrollern kan man läsa att dessa är externa I/O-register (UCSR0A och UDR0) som har med USART att göra.

Värdet som skrivs kommer från R18 vilket läses från `Y+1` vid 0x009a. Värdet vid `Y+1` kommer från R24 vid 0x008c. Den senaste skrivningen till R24 var av main() precis innan anropet till den inre funktionen:
```
  006a subi R24,0x0
  006b sbci R25,0xff
  006c movw Z,R25R24
  006d ld   R25,Z
  006e lds  R24,DAT_mem_0134
  0070 eor  R24,R25
  0071 call FUN_code_000087
```

0x006e läser in en konstant (0x42) från .data-segmentet och 0x0070 XOR:ar denna konstant med värdet i R25 som läses från Z vid 0x006d. Z-registret inkrementeras i en loop. Det initiala värdet på Z-registret i början av loopen är inte så lätt att hitta, men enligt Ghidra finns det bara två referenser till .data-segmentet: adressen som lagrar konstanten 0x42, och en sekvens med 52 bytes. Att använda 0x42 som XOR-nyckel för att avkoda sekvensen ger samma utdata som skrivs ut om man kör programmet. Ledtråden i beskrivningen tyder på att den här nyckeln kan vara fel. Med t.ex. CyberChefs "XOR brute force"-modul kan rätt nyckel hittas (0x71) som ger en sträng som börjar med "cratectf{".
