#!/usr/bin/env python3
# Porovnavani prvku seznamu

# fce vrati True nebo False podle toho, zda jsou dane dva seznamy
# stejne az na poradi prvku. Prvky se nemohou opakovat
def porovnaniSeznamu(seznam1, seznam2):
	return set(seznam1) == set(seznam2)

# fce vrati True nebo False podle toho, zda jsou dane dva seznamy
# stejne az na poradi prvku. Prvky se mohou opakovat
def porovnaniSeznamuOpakovani(seznam1, seznam2):
	# Seznam seradime, abychom mohli porovnat seznamy s prehazenymi prvky
	return sorted(seznam1)==sorted(seznam2)

# Pomocna funkce, ktera pripravi slovnik cetnosti cisel v seznamu
def pripravSlovnik(seznam):
	slovnik = {}
	for c in seznam:
		if c in slovnik:
			slovnik[c] += 1
		else:
			slovnik[c] = 1
	return slovnik

def porovnaniSeznamuSlovnik(seznam1, seznam2):
	# Rychlejsi reseni predchozi ulohy s vyuzitim slovnikum:
	# pripravime slovniky s cetnosti jednotlivych cisel a ty pak porovname
	slovnik1 = pripravSlovnik(seznam1)
	slovnik2 = pripravSlovnik(seznam2)
	return slovnik1 == slovnik2

# fce vrati True nebo False podle toho, zda jsou vsechny prvky seznamu navzajem ruzne
def ruznePrvky(seznam):
	return(len(seznam)==len(set(seznam)))
