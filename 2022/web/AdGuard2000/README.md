# AdGuard 2000
Webtjänst med sql-injection sårbarheter.

Apache + php + sqlite används. Databasen genereras från en sql-dump vid skapandet av containern.
Ingen lagring utanför containern, så en restart nollställer tjänsten enkelt om någon har sönder den.
