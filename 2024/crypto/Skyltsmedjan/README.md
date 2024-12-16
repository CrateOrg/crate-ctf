# Skyltsmedjan
Utmaningen bygger på https://en.wikipedia.org/wiki/Digital_signature_forgery.<br> 
Kortfattat beskriver artikeln att om du kan signaturen till m1 och m2, kan du beräkna signaturen för m1*m2.<br>
Tjänsten signerar meddelanden, men inte de som innehåller `flag`. För att få behörighet till flaggan krävs det att man stoppar in: 
```python
msg = f"Kund nr. {userid} får hämta flaggan".encode("utf-8")
```
Genom att faktorisera `msg` kan man få programmet att signera dessa m1 och m2, detta medger att man kan förfalska signaturen till `msg`. <br> 
$\displaystyle \sigma \left(m'\right)=\sigma (m_{1}\cdot m_{2})=\sigma (m_{1})\cdot \sigma (m_{2})$
Se solve.py för full lösning.
