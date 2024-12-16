# Buggigt

En GDB-session där ett program har fastnat i ett segmenteringsfel. Funktionen `print_flag()` ska skriva ut flaggan, men den kraschar på grund av att mode-argumentet till `fopen()` är "open" istället för "r" (för "read").

GDB visar att kraschen skedde i `_IO_getc()` och att filpekaren var satt till NULL (`fp=0x0`), därav segmenteringsfelet:
```
(gdb) backtrace
#0  0x0000728a7bb18ce9 in _IO_getc (fp=0x0) at ./libio/getc.c:37
#1  0x00005dba2dc3f1b7 in print_flag ()
#2  0x00005dba2dc3f1ec in main ()
```
Hela `print_flag()`-funktionen ser ut så här:
```
Dump of assembler code for function print_flag:
   0x00005dba2dc3f179 <+0>:	push   rbp
   0x00005dba2dc3f17a <+1>:	mov    rbp,rsp
   0x00005dba2dc3f17d <+4>:	sub    rsp,0x10
   0x00005dba2dc3f181 <+8>:	lea    rax,[rip+0xe7c]        # 0x5dba2dc40004
   0x00005dba2dc3f188 <+15>:	mov    rsi,rax
   0x00005dba2dc3f18b <+18>:	lea    rax,[rip+0xe77]        # 0x5dba2dc40009
   0x00005dba2dc3f192 <+25>:	mov    rdi,rax
   0x00005dba2dc3f195 <+28>:	call   0x5dba2dc3f060 <fopen@plt>
   0x00005dba2dc3f19a <+33>:	mov    QWORD PTR [rbp-0x8],rax
   0x00005dba2dc3f19e <+37>:	jmp    0x5dba2dc3f1ab <print_flag+50>
   0x00005dba2dc3f1a0 <+39>:	movsx  eax,BYTE PTR [rbp-0x9]
   0x00005dba2dc3f1a4 <+43>:	mov    edi,eax
   0x00005dba2dc3f1a6 <+45>:	call   0x5dba2dc3f030 <putchar@plt>
   0x00005dba2dc3f1ab <+50>:	mov    rax,QWORD PTR [rbp-0x8]
   0x00005dba2dc3f1af <+54>:	mov    rdi,rax
   0x00005dba2dc3f1b2 <+57>:	call   0x5dba2dc3f070 <getc@plt>
=> 0x00005dba2dc3f1b7 <+62>:	mov    BYTE PTR [rbp-0x9],al
   0x00005dba2dc3f1ba <+65>:	cmp    BYTE PTR [rbp-0x9],0xff
   0x00005dba2dc3f1be <+69>:	jne    0x5dba2dc3f1a0 <print_flag+39>
   0x00005dba2dc3f1c0 <+71>:	mov    rax,QWORD PTR [rip+0x2e71]        # 0x5dba2dc42038 <stdout@GLIBC_2.2.5>
   0x00005dba2dc3f1c7 <+78>:	mov    rdi,rax
   0x00005dba2dc3f1ca <+81>:	call   0x5dba2dc3f050 <fflush@plt>
   0x00005dba2dc3f1cf <+86>:	mov    rax,QWORD PTR [rbp-0x8]
   0x00005dba2dc3f1d3 <+90>:	mov    rdi,rax
   0x00005dba2dc3f1d6 <+93>:	call   0x5dba2dc3f040 <fclose@plt>
   0x00005dba2dc3f1db <+98>:	nop
   0x00005dba2dc3f1dc <+99>:	leave
   0x00005dba2dc3f1dd <+100>:	ret
```
Att filpekaren var NULL tyder på att något gick fel i öppnandet av filen (`fopen()`), så vi kan kolla på argumenten till den funktionen med hjälp av adresserna som GDB skrivit ut som kommentarer innan anropet till `fopen()`:
```
(gdb) x/s 0x5dba2dc40004
0x5dba2dc40004:	"open"
(gdb) x/s 0x5dba2dc40009
0x5dba2dc40009:	"/flag.txt"
```

De förekommer i omvänd ordning, men från t.ex. https://en.cppreference.com/w/c/io/fopen går det att se att "mode"-argumentet ska vara "r", "w", "a", osv. för "read", "write", "append". "open" som programmet försöker använda är fel, så vi kan byta ut det genom att sätta en breakpoint på `print_flag()`, starta om programmet, stega fram till efter att argumenten skrivits men innan `fopen()` anropas och byta ut strängen. Sök t.ex. på "gdb overwrite string variable" för detaljer kring det. Använd t.ex. `layout asm` för att se vilken instruktion som körs och stoppa vid rätt tillfälle (`0x00005dba2dc3f195` i exemplet ovan).

```
Program received signal SIGSEGV, Segmentation fault.
0x000078b2c94c0ce9 in _IO_getc (fp=0x0) at ./libio/getc.c:37
37	./libio/getc.c: No such file or directory.
(gdb) break print_flag
Breakpoint 1 at 0x632d1590417d
(gdb) run
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/ctf/main 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x00005dba2dc3f179 in print_flag ()
(gdb) nexti
(gdb) nexti
(gdb) nexti
(gdb) nexti
(gdb) nexti
(gdb) x/s 0x5dba2dc40004
0x5dba2dc40004:	"open"
(gdb) set {char [2]} 0x5dba2dc40004 = "r"
(gdb) x/s 0x5dba2dc40004
0x5dba2dc40004:	"r"
(gdb) continue
Continuing.
cratectf{riktigt_bra_avlusat}
```
