# Fillagringstjänst

`cookieParser.signedCookie` validerar att en cookie är korrekt signerad och
returnar bara `false` om inte. Men om den inte är signerad alls (börjar med
`s:`) så bara returnar den det man stoppade in, så man kan ändra sin session
cookie till vad som helst som inte börjar på `s:`. Till exempel `../..`, sen är
det bar att trycka på `flag.txt` för att ladda ner flaggan.
