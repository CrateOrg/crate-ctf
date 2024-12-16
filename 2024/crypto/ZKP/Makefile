main:
	sed "s/FAKEFLAG/pirat1_var_långt_från_pirat2_när_kon_levererades/" main.c | tee mainFlag.c 
	gcc -o docker/main mainFlag.c -lgmp
	rm mainFlag.c

.PHONY: main
