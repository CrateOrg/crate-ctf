#!/bin/bash
while true;
do
    curl https://handla.api.ica.se/api/recipes/random?numberofrecipes=1 > recept.json
    python3 cleanjson.py recept.json >> rena_recept.json
done
