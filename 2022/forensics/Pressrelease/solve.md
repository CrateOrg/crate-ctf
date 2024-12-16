# Lösningsförslag
Eftersom vim används så är det nog svårt att manuellt följa varje knapptryck, även om det går!
Min lösning var att via virtualbox injicera knapptryckningar.

Skapa script; denna variant råkar bli powershell, för användning i en virtualbox-maskin som heter ESP-Dev:
echo "\$sleepval=100" > replay.ps1 && cat pressrelease.txt | tr " " "\n" | grep -v "^$" | sed s/0x// | xargs -I fff echo ".\VBOXManage controlvm \"ESP-Dev\" keyboardputscancode fff ; sleep -Milliseconds \$sleepval" >> replay.ps1

För bash:
echo "sleepval=0.02" > replay.sh && cat press2.txt | tr " " "\n" | grep -v "^$" | sed s/0x// | xargs -I fff echo "vboxmanage controlvm \"lore 20.04\" keyboardputscancode fff ; sleep \$sleepval" >> replay.sh

Starta sedan en terminal i din VM, och kör scriptet ute i hosten. Ta-da!
