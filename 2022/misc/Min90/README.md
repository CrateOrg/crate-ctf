# Min 90

En a-traktor har installerat 10 stycken dotmatrix-displayer och styr alla via modbus.
Datan för texten som ska rulla på displayerna ligger i tillgänglig via slavarnas input registers.
register 0 = pixel height
register 1 = pixel width

Datat (packat som bytes) börjar på register 240.

Flaggdisplayen har id 0x1f (bakre displayen).

Utöver detta sitter en "injektorbrygga" med id 0x33. På holding register 0xb lagras den maximala tillåtna hastigheten.
Den är default 30, men när den sätts till 90 eller mer aktiveras möjligheten att läsa ut input-registers för flagg-displayen.
Vid set(maxspeed) startar en 10 sekunders timer som vid expiry sätter tillbaka maxhastigheten till 30km/h.


