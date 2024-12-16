# Långtidsminne

Minnesdumpen kommer från en VM där programmet `C:\Users\Administrator\Downloads\metasploit_psexec_session_stager.exe` har körts vid 2024-08-23 14:12:29. Filen kan efter uppackning (med `gzip -d memdump.elf.gz`) analyseras med t.ex. [Volatility](https://github.com/volatilityfoundation/volatility). Då processen redan har avslutats går det dock inte att hitta något med de vanliga funktionerna för att lista processer (`windows.pslist` eller `windows.psscan`). Tyvärr verkar det vara lite svårt att hitta rätt kommando med en webbsökning, men om man kollar på t.ex. den här cheat-sheet:ens lista över process-relaterade kommandon så finns `windows.registry.userassist` med beskrivningen:
>Windows keeps track of programs you run using a feature in the registry called UserAssist keys. These keys record how many times each program is executed and when it was last run.  
https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/memory-dump-analysis/volatility-cheatsheet#processes

Att köra det på minnesdumpen visar många program som har körts (bland annat `%windir%\system32\SnippingTool.exe`, `%windir%\system32\mspaint.exe` och `%windir%\system32\Sysprep\sysprep.exe`), men bara ett av programmen (med det suspekta namnet `metasploit_psexec_session_stager.exe`) kommer från Administrator:s mapp för nedladdade filer.
```
sudo vol -f memdump.elf windows.registry.userassist           
Volatility 3 Framework 2.7.0
Progress:  100.00		PDB scanning finished                        
Hive Offset	Hive Name	Path	Last Write Time	Type	Name	ID	Count	Focus Count	Time Focused	Last Updated	Raw Data

0xdf0786ca4000	hive0xdf0786ca4000	-	-	-	-	-	-	-	-	-	-
0xdf0786e37000	hive0xdf0786e37000	-	-	-	-	-	-	-	-	-	-
[...]
* 0xdf078839e000	\??\C:\Users\Administrator\ntuser.dat	ntuser.dat\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{CEBFF5CD-ACE2-4F4F-9178-9926F41749EA}\Count	2024-08-23 14:12:29.000000 	Value	%windir%\system32\SnippingTool.exe	N/A	14	21	0:07:00.500000	2021-06-10 08:07:27.000000 	
[...]
* 0xdf078839e000	\??\C:\Users\Administrator\ntuser.dat	ntuser.dat\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{CEBFF5CD-ACE2-4F4F-9178-9926F41749EA}\Count	2024-08-23 14:12:29.000000 	Value	%windir%\system32\mspaint.exe	N/A	2	3	0:01:00.500000	2021-06-10 08:07:27.000000 	
[...]
* 0xdf078839e000	\??\C:\Users\Administrator\ntuser.dat	ntuser.dat\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{CEBFF5CD-ACE2-4F4F-9178-9926F41749EA}\Count	2024-08-23 14:12:29.000000 	Value	Microsoft.Windows.Explorer	N/A	4	3	0:01:22.314000	2024-08-23 14:11:55.000000 	
[...]
* 0xdf078839e000	\??\C:\Users\Administrator\ntuser.dat	ntuser.dat\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{CEBFF5CD-ACE2-4F4F-9178-9926F41749EA}\Count	2024-08-23 14:12:29.000000 	Value	%windir%\system32\Sysprep\sysprep.exe	N/A	0	1	0:01:13.844000	N/A	
[...]
* 0xdf078839e000	\??\C:\Users\Administrator\ntuser.dat	ntuser.dat\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{CEBFF5CD-ACE2-4F4F-9178-9926F41749EA}\Count	2024-08-23 14:12:29.000000 	Value	MSEdge	N/A	2	7	0:04:48.219000	2024-08-22 14:55:53.000000 	
[...]
* 0xdf078839e000	\??\C:\Users\Administrator\ntuser.dat	ntuser.dat\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{CEBFF5CD-ACE2-4F4F-9178-9926F41749EA}\Count	2024-08-23 14:12:29.000000 	Value	Microsoft.Windows.Search_cw5n1h2txyewy!CortanaUI	N/A03	0:00:29.264000	N/A	
[...]
* 0xdf078839e000	\??\C:\Users\Administrator\ntuser.dat	ntuser.dat\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{CEBFF5CD-ACE2-4F4F-9178-9926F41749EA}\Count	2024-08-23 14:12:29.000000 	Value	C:\Users\Administrator\Downloads\metasploit_psexec_session_stager.exe	N/A	1	0	0:00:00.515000	2024-08-23 14:12:27.000000 	
```

## Skapande av minnesdump
Minnesdumpen skapades manuellt från `win10-ent21h1-x64-clean.src` genom att:
1. Starta maskinen i QEMU/virt-manager (testat med 4 GB RAM). Ta gärna en snapshot först eftersom det kan vara svårt att rensa bort tidigare spår ifall de här stegen upprepas.
2. Kopiera in valfri .exe via en monterad .iso-fil (`mkisofs -o disk.iso my_directory`). Döp om den till rätt namn. En delad mapp (via hypervisorn) kanske också fungerar.
3. Kör .exe:n genom att dubbelklicka på den i utforskaren. Andra sätt att starta filen kanske inte skapar rätt registernycklar för att den ska kunna hittas i minnesdumpen.
4. Ta en minnesdump med `sudo virsh dump <VM_NAMN> --memory-only --verbose --format=elf memdump.elf`.
5. Komprimera den med `gzip memdump.elf`.

Ibland dök inte registernycklarna upp så att Volatility hittade programmet, testa i så fall att ta bort minnesdumpen, köra programmet igen och ta en ny minnesdump.
