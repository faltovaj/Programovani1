"""
Nahodna prochazka v 1D:
- V kazdem kroku cislo zvysime nebo snizime o 1, na pozici 0 pouze zvysujeme
- Kolik kroku potrebujeme, abychom se dostali do N?
"""

import random as r

N = int(input('Zadejte koncovou pozici (prirozene cislo): '))
pozice = 0
N_krok = 0

#r.seed(12457)
while pozice < N:
    if pozice == 0:
        pozice += 1
    else:
        pozice += r.choice([-1,1])
    N_krok += 1

print(f'Pocet kroku je {N_krok}')