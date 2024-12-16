# Protokollkoll

En server som implementerar ett litet TLV (type-length-value)-protokoll:
<table>
  <thead>
    <tr>
      <th>Byte: </th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3+Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="1"></td>
      <td colspan="1">Type (uint8)</td>
      <td colspan="2">Length (uint16)</td>
      <td colspan="1">Value (UTF-8)</td>
    </tr>
  </tbody>
</table>

Servern svarar med lite olika skräpdata beroende på vilken data som skickas till den och vilken typ (0-2) som anges. Typ 5 ger flaggan som svar och övriga typer ger "Error". En PCAP-fil finns given där typ 0-3 skickas. Typ- och längdfälten kan då identifieras genom att kolla på konversationerna i PCAP:en. Genom att skriva ett litet skript kan olika typer testas tills flaggan hittas.
