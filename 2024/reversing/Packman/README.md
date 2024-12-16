# Packman
En tjänst där man laddar upp filer, och sedan packar dem. Formatet följer byte, short: Där det motsvarar offset, count. <br>

data.txt: 
```
00000000: 4141 4141 4141 4242 4242 4343 4343 0a00  AAAAAABBBBCCCC..
00000010: fffe 410a                                ..A.
```
data.packed: <br>
```
00000000: f100 06f2 0004 f300 04ba 0001 b000 01af  ................
00000010: 0001 ae00 01f1 0001                      ........
```
Genom att kika på data.packed kan man se f1,f2,f3 är ett ifrån varandra, samma skillnad som A,B,C. Efter f1 kommer 0006 då som är 6 A:n. Om man istället tittar på byte 10 i data.txt som är 0xff, blir enkodat till 0xaf. `0xff - 0xaf = 0x50`. Eftersom A (0x41) är mindre än 0x50, fast i data.packed har den ett större värde.<br> 
```
data.txt:
0x41 < 0xff
data.packed
0xf1 > 0xaf
```
Kan det tolkas som att byten som står i data.packed är en offset från den konstanta byten 0x50, men det wrappar runt offseten som en ring buffer, därför är offseten större till 0x41 än till 0xff.
```
Offseten wrappar runt efter 0xff: 
<---------------------------------------|
|                                       |
+1+1+1+1+1+1+1->        1+1+1+1+1+1+1+1->
0x00, 0x01 .. 0x41 ... 0x50... 0xfe, 0xff
```
Genom att använda denna algoritmen på flag.packed (se solve.py), så får man ut en ELF-fil som skriver ut flaggan.
