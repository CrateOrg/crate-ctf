# Max 30

En a-traktor har installerat 10 stycken dotmatrix-displayer och styr alla via modbus.
Datan för texten som ska rulla på displayerna ligger i tillgänglig via slavarnas input registers.
register 0 = pixel height
register 1 = pixel width

Datat (packat som bytes) börjar på register 240.

Matrisen på adress 0x19 har en flagga som text.
