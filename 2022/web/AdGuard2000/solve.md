# Logga in
Password-fältet på loginsidan kan utsättas för SQL-injections! 

Flera olika sätt att logga in (admin har id 9)
* mha id
  ' or id=1;--       
* mha användarnamn
  ' or username like 'admin';--

# Hitta hemligheten
Är man inne som admin presenteras en länk till "manageusers.php", annars kan man hitta bortkommenterad länk i menyn.
Man måste vara inloggad som admin för att komma åt manageusers.php! Antingen testar man 1.....9 eller så kör man enligt alternativ #2 ovan.

SQL-injections kan användas för sökning av användare. (OBS här är det " istället för ' :-)
* Hitta vilka tabeller som finns:
  " union select 1,1,1,sql from sqlite_master;--
* Secrets tabellen ser ju intressant ut, kolumn secret:
  " union select 1,1,1,secret from secrets;--
* Läs alla rader, eller sök på cratectf - WIN!
