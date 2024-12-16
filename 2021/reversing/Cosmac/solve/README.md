larhel's way of solving, stealing code from https://github.com/JamesGriffin/CHIP-8-Emulator.git
Build with make, depends on SDL2.

Start with ./chip8 ../protected.ch8

Initial PIN is 0000. Current pin printed on stdout.

Right arrow   PIN+=1
Up arrow      PIN+=10
Left arrow    PIN-=1
Down arrow    PIN-=10
ESC           exit

Tobias found out why several PIN's are accepted:
Om man har pinkod ABCD så verkar det som att flaggan kommer skrivas ut om A^C == 7, B^D == 4, och A^D == 5, vilket är ett system som har många lösningar.

https://git.crate.foi.se/capturetheflag/foi-ctf-2021/-/blob/master/challenges/Cosmac/challenge.asm#L54

V0 innehåller första tecknet från den obfuskerade flaggan, V1 innehåller första siffran i pinkoden, V3 innehåller tredje siffran i pinkoden.
Så den tar V0 ^ V1 ^ V3 för att räkna ut vilket tecken den ska skriva ut.

Finns flera grejer man kan stoppa in i V1 och V3 och ändå få samma resultat.
Alla de här borde enligt mig skriva ut flaggan, i så fall:
0 1 7 5
1 0 6 4
2 3 5 7
3 2 4 6
4 5 3 1
5 4 2 0
6 7 1 3
7 6 0 2
8 9 15 13
9 8 14 12
10 11 13 15
11 10 12 14
12 13 11 9
13 12 10 8
14 15 9 11
15 14 8 10
