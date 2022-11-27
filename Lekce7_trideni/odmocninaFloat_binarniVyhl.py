#!/usr/bin/env python3
# Celociselna odmocnina pomoci binarniho vyhledavani

epsilon = 1e-10

def odmocnina(cislo):
    min = 0                            # hledame v intervalu indexu [min, max]
    max = cislo              

    while (max-min) >= epsilon:
        stred = (max + min)/2     # poloha uprostred prohledavaneho useku
        kandidat = stred * stred
        if kandidat < cislo:  # hledani pokracuje napravo
            min = stred
        else:                            # hledani pokracuje nalevo
            max = stred
    else:
        print(f"Odmocnina lezi mezi {min} a {max}")

vstup = int(input("Zadejte cislo, kteremu chcete urcit celociselnou odmocninu "))
odmocnina(vstup) 
