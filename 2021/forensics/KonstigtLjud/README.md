Utmaningen består av en bild som har kodats i [APT-format](https://en.wikipedia.org/wiki/Automatic_picture_transmission), vilket sedan 1964 har använts för att skicka bilder från vädersatelliter. Idag används nyare metoder, men det finns fortfarande satelliter som sänder i detta format och mjukvara för avkodning finns fritt tillgänglig.

Avkodare:
* https://wxtoimgrestored.xyz/
* https://github.com/martinber/noaa-apt
* Webbaserad: https://jthatch.com/APT3000/APT3000.html

source.pgm innehåller källbilden tillsammans med en QR-kod, vilken har kodats med [https://github.com/gkbrk/apt-encoder]():

```
./apt-encode source.pgm source.pgm > encode.raw
sox -t raw -b 8 -e unsigned -c 1 -r 12480 encode.wav -r 11025 chall.wav
```
Extra brus och bakgrundljud har sedan lagts till.
