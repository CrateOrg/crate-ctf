# Kassaskåpet

Utmaningen är ett smart kontrakt som deployats på en lokal blockkedja. Vid skapandet av kontraktet så sätts ett lösenord och man kan byta ägare av kontraktet genom att ge lösenordet. När man äger kontraktet kan man även hämta ut flaggan.
<br>
Man skulle kunna tro att "private" nyckelordet är privat och kan därför inte läsas utifrån, det kan inte kallas direkt från kontraktets ABI till skillnad från "public". Dock så ligger datan fortfarande på blockkedjan, genom att analysera minnet för det kontraktet så kan man läsa ut den lokala variabeln.  
<br>
Se lösning i solve.py. 
<br> 
