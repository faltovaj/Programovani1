#!/usr/bin/env python3
# Binarni vyhledavani v serazenem seznamu

# Prvni verze s cyklem
def binarniVyhledavani(seznam, hodnota):
	i_min = 0                            # hledame v intervalu indexu [i_min, i_max]
	i_max = len(seznam) - 1              

	while (i_max - i_min) >= 0: 
		i_stred = (i_max + i_min)//2     # poloha uprostred prohledavaneho useku
		#print(f'[{i_min},{i_max}] {i_stred}')
	        if seznam[i_stred] == hodnota:   # nalezli jsme hledane cislo
			print("Hodnota", hodnota, "nalezena na pozici", i_stred)
			return i_stred
		elif seznam[i_stred] < hodnota:  # hledani pokracuje napravo
			i_min = i_stred + 1
		else:                            # hledani pokracuje nalevo
			i_max = i_stred - 1
	else:                                # hledana hodnota v seznamu neni
		print("Cislo", hodnota, "v seznamu neni.")


# Druha verze s rekurzi
def binarniVyhledavani_rekurze(seznam, i_min, i_max, hodnota):
	if i_min > i_max:                # hledana hodnota v seznamu neni
		print("Cislo", hodnota, "v seznamu neni.")
		return
	i_stred = (i_max + i_min)//2     # poloha uprostred prohledavaneho useku
	if seznam[i_stred] == hodnota:   # nalezli jsme hledane cislo
		print("Hodnota", hodnota, "nalezena na pozici", i_stred)
		return i_stred
	elif seznam[i_stred] < hodnota:  # hledani pokracuje napravo
		binarniVyhledavani_rekurze(seznam, i_stred + 1, i_max, hodnota)
	else:	
		binarniVyhledavani_rekurze(seznam, i_min, i_stred - 1, hodnota)

