chall.pcapng innehåller en paketdump av trafiken från ett WPA2-krypterat trådlöst nätverk med lösenordet "password123". Genom att använda t.ex. aircrack-ng borde lösenordet gå att hitta inom några sekunder även med en liten ordlista. Wireshark kan sedan användas för att dekryptera trafiken med hjälp av lösenordet. Ett ICMP-paket har skickats från 192.168.1.3 till 192.168.1.2, detta innehåller flaggan.

Nätverket simulerades med hjälp av mac80211_hwsim och hostapd.

hostapd.conf:
```
interface=wlan0
ssid=CTF-testnet
wpa=2
wpa_passphrase=password123
wpa_key_mgmt=WPA-PSK
```
ICMP-paketet skickades med `hping3 -1 -E ./flag.txt -d 256 -u -I wlan1 192.168.1.2`.
