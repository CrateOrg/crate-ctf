# IAX

Nätverksdump med blandad trafik: ssh, https och ett SIP-samtal.
För att göra utmaningen något svårare är sjävla SIP-inviten borttagen.
Man måste själv identifiera att det går RTP-trafik, t.ex. genom att se RCTP-paketen.

RTP-strömmen kör G711 codec som wireshark har stöd för att spela upp:

- Hitta ett RTP-paket
- Välj "decode as" -> RTP
- Gå till telephony -> RTP -> RTP Streams
- Analyze och play

## Lite om tillverkningen
support   @ 148.94.181.10
user      @ 148.94.52.90
downloader@ 148.94.102.45

support:
pjsua-x86_64-unknown-linux-gnu --no-vad --rtp-port 49822 --null-audio --auto-play --auto-play-hangup --play-file /root/supporten.wav --dis-codec=speex --dis-codec=iLBC --dis-codec=gsm

user:
pjsua-x86_64-unknown-linux-gnu --no-vad --rtp-port 54829 --null-audio --auto-play --auto-play-hangup --play-file /root/fiapia.wav --dis-codec=speex --dis-codec=iLBC --dis-codec=gsm

downloader:
httrack https://www.linkedin.com/ -s0 -A7000 --user-agent "Mozilla"
ssh till temporär digitalocean-droplet

sudo tcpdump -i br-sipcall -s0 -w dump.pcap
