# KaKlickare
Tanken är att detta ska vara en lättare uppvärmnings uppgift. <br>
När kakan har klickats 1 miljard gånger så skickas flaggan. Mängden gånger som den har klickats är bestämt utav kak parametern "clicks" i post förfrågningen. <br>

## Lösning
`echo -n '1000000000' | base64 | xargs -i{} curl -X POST --cookie "clicks={}" http://localhost:50012/flag.php`
Man kan också gå in i dev consolen och sätta variabeln till det värdet.
