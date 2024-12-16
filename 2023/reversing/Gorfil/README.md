# Görfil

## Lösning

När `make check` körs körs först `format` och `contents`.

`format` använder grep för att plocka ut flaggformatet, alltså `cratectf{` och `}` (om de finns).

`contents` gör ett nestlat anrop till make som använder `subst` för att plocka bort `cratectf{` och `}`.

Sedan i `check` körs `stage1` som gör så att flaggformatets sha1-summa skrivs till filen vars namn är formatets sha1-hmac.

Sedan körs `stage2`, som kräver en fil med namnet samma som innehållet i `eae2a8e65aa2326a64475835648d846e44d8fdd4`. Lyckas man gissa att flaggformatet är `cratectf{}` (vilket går att se i makefilen) får man att filen `eae2a8e65aa2326a64475835648d846e44d8fdd4` innehåller `8d7b5bef406384883fe0f30e066339817c05712a`. I det fallet kommer regeln på rad 20 skriva `hej` till `8d7b5bef406384883fe0f30e066339817c05712a`, och lyckas make med `stage2`.

`check` kör sedan `make constraints` som har ett antal förkrav.

Den första, `setrlimit` kör ett komprimerat pythonprogram som kollar att alla tecken i flaggan (med formatet borttaget) är små latiska bokstäver.

Resten följer mönstret av ett `x`, ett antal `a`:n och sist ett namnet på olika linux syscalls. Dessa skapas av regeln strax ovan i filen. De reglerna använder sig av funktionerna `d` och `sub`. `sub` byter ut en förekomst av första parametern till andra parametern i den tredje. `d` läser den n:te bokstaven ut flaggan och ger ut ett `a` för ett `a`, två `a`:n för ett `b`, tre `a`:n för att `c`, osv. Med dessa kan vi lösa ut en bokstav i taget.

`x$(call d,1)getpgrp` och `xaaagetpgrp` ger oss att flaggans första bokstav är c.

`x$(call d,2)aaaprctl` och `xaaaaaaaaaaaprctl` ger oss att flaggans andra bostav är `h`.

`x$(call d,3)$(call d,3)tuxcall` och `xaaaaaaaaaatuxcall` ger oss att tredje bokstaven är `e`.

`x$(call sub,$(call d,1),,$(call d,4))$(call sub,$(call d,2),,$(call d,7))$(call sub,$(call d,3),,$(call d,8))dup3` och `xdup3` ger oss att den första och fjärde bokstaven är samma (c), att andra och sjunde är samma (h) och att tredje och åttonde är samma (e).

`x$(call sub,$(call d,4),,$(call d,6))openat` och `xaaaaaaaaaaaaaaaaaopenat` ger att den sjätte bokstaven är `t`.

`x$(call d,5)$(call d,8)syncfs` och `xaaaaaaaaaaaaaaaasyncfs` ger att femte bokstaven är `k`.

`x$(call d,9)aachroot` och `xaaaaaaaachroot` ger att nionde bokstaven är `f`.

`x$(call d,12)$(call sub,$(call d,7),$(call d,3),$(call d,9))swapoff` och `xaaaaaaaaaaaaaswapoff` kan verka ge att tolfte bokstaven är `l`, men eftersom sjunde bokstaven (h) kommer senare i alfabetet än nionde (f) görs ingen substition och tolfte bokstaven är därmed `g`.

`x$(call sub,$(call d,11),$(call d,6),$(call d,1))socket` och `xaaaaaaaaaaaaaaaaaaaaaasocket` ger att elfte bokstaven är `a`.

`x$(call d,10)$(call d,11)fallocate` och `xaaaaaaaaaaaaafallocate` ger att tionde bokstaven är `l`.

Tillsammans ger detta `cratectf{checktheflag}`.
