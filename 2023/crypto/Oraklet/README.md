# Oraklet

En dekrypteringstjänst som användes AES-CBC för att avkoda några meddelanden som ges i uppgiften. Tjänster låter en inte läsa meddelandet som innehåller flaggan, men berättar ifall meddelandet dekrypterades korrekt (den PKCS #7 padding som mottogs var korrekt) eller inte. En [padding oracle attack](https://en.wikipedia.org/wiki/Padding_oracle_attack) kan användas för att dekryptera meddelandet och få ut flaggan.
