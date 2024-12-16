#!/bin/bash
# Ge den text som ska färgkodas som indata till skriptet i en separat textfil.
# Texten får bara innehålla ascii-tecken och längden ska vara jämnt delbar med 3.
# Max längd är 999999 tecken.

langd=$( wc -c $1 | cut -d " " -f1 )
testar=$( echo ${langd}%3 | bc )
if [ ${testar} -eq 0 ] && [ ${langd} -lt 1000000 ]
then
    for i in $( cat $1 | xxd -g3 -c 36 | cut -d " " -f2-12 | tr " " "\n" | nl -n rz -s "#" | tr -s " " | cut -d " " -f2- )
    do namn=$( echo ${i} | cut -d "#" -f1 )
       strang=$( echo ${i} | cut -d "#" -f2 )
       convert -size 64x64 xc:#${strang} ${namn}.png
    done
else
    echo "Fel längd! Ska vara jämnt delbart med 3 och mindre än 1000000. Se upp för automatiska radbrytningar!"
fi
