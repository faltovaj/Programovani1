#!/usr/bin/env python3
# Celociselna odmocnina pomoci binarniho vyhledavani

def odmocnina(cislo):
	min = 1                            # hledame v intervalu indexu [min, max]
	max = cislo              

	while max >= min:
		stred = (max + min)//2     # poloha uprostred prohledavaneho useku
		kandidat = stred * stred
		if kandidat == cislo:   # nalezli jsme hledanou odmocninu
			print("Odmocnina je", stred)
			return stred
		elif kandidat < cislo:  # hledani pokracuje napravo
			min = stred + 1
		else:                            # hledani pokracuje nalevo
			max = stred - 1
	else:                                # hledana hodnota v seznamu neni
		print(f"Cislo nema celociselnou odmocninu.")

vstup = int(input("Zadejte cislo, kteremu chcete urcit celociselnou odmocninu "))
odmocnina(vstup)
