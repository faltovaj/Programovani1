#!/usr/bin/env python3
# Trideni vyberem (opakovany vyber minima)

def trideniVyberem(seznam):
    for i in range(len(seznam)):                # Vnejsi cyklus pres vsechny prvky seznamu
        i_min = i                               # Seznam je do i-teho prvku uz serazeny
        for j in range(i+1, len(seznam)):       # Vnitrni cyklus: hledame minimum v nesetridenem podseznamu
            if seznam[j]<seznam[i_min]:
                i_min = j
        seznam[i], seznam[i_min] = seznam[i_min], seznam[i]      # Minimum prijde na 1. nesetridene misto
                                                                 # a prvek na tomto miste na misto minima
    return seznam

seznam = [7, 480, 5, 6, 2, 400, 3, 8, 6, 10, 1, 15, 0]
print(f"Nesetrideny seznam {seznam}")
print(f"Setrideny seznam {trideniVyberem(seznam)}")
