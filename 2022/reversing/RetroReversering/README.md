Ett simpelt intro för gameboy.
Knapparna A och B kan användas för att knappa in en 1-bit respektive en 0-bit.
Efter varje knapptryckning uppdateras den scrollande texten baserat på vad som knappas in.
Genom att knappa in 8 korrekta bitar i sekvens erhålles det korrekta startvärdet för "dekrypteringsfunktionen" (0xA3=0b10100011) och texten kommer att bli flaggan.
Notera att bitarna måste knappas in i gameboy-indianer, så korrekt inmatning är: 1 1 0 0 0 1 0 1 = A A B B B A B A.
