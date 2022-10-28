#!/usr/bin/env python3
# Eratosthenovo sito: algoritmus na vypsani prvocisel mensich nez N

N = int(input("Zadejte do jakeho cisla chcete vypsat prvocisla: "))
# Pripravim si sito:
# - index seznamu je testovane cislo
# - True - cislo mame stale v seznamu (na zacatku mame vsechna cisla v seznamu)
# - False - cislo jsme ze seznamu vyjmuli
sito = [True] * (N+1)

for i in range(2,N+1):
    if sito[i]:      # pokud cislo v seznamu je
        print(i)     # prvni cislo je prvocislo
        for j in range(2*i, (N+1), i):    # cyklus pres nasobky daneho cisla
            sito[j] = False               # nasobky ze seznamu vyjmeme
