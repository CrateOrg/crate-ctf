# Red teaming?

Tanken är att detta ska vara en uppvärmningsuppgift då den kräver minimalt skriptande.
Binärdatan är infraröda signaler tagna från en Samsung TV-kontroll. När man söker på "IR-remote codes github" är detta väldigt högt upp: https://github.com/lepiaf/IR-Remote-Code <br>
Modellen kan gissas eftersom det är väldigt mycket `0xe0e0...` i datan. I datan så följer mönstret (ASCII kod)(mute)(ASCII kod). Konvertera decimalerna till ASCII så får man ut flaggan.
## Göra svårare?
Eftersom mätningarna är gjorda över tid så kan man för att göra det realistiskt slänga in random null bytes lite här och var. <br>
Eller på något sätt ge mätningen i form av ett diagram.
