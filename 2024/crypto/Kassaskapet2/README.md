Utmaningen är ett smart kontrakt som deployats på en lokal blockkedja. När man äger kontraktet kan man även hämta ut flaggan.
<br>
Eftersom random-funktionen nyttjar sig av blockhashen så kan man beräkna i förhand vad den kommer att returnera. Checken tx.origin != msg.sender medger att man måste deploya ett proxykontrakt att agera genom. 
<br>
Se lösning i solve.py, Samt Exploit.sol.
