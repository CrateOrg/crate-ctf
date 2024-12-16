# Sök

En mongodb-injection som låter en filtrera på användares lösenord (som sparas i
klartext).

Kan göras svårare genom att inte ge ut källkoden.

Kan också göras svårare genom att spara lösenordshashar i databasen då man
också måste knäcka hashen. T.ex. kan man slumpa lösenord från rockyou. Kan då
vara passande att rate-limita inloggningsförsök.
