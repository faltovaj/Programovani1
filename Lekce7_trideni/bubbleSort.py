#!/usr/bin/env python3
# Bublinkove razeni (prohazujeme sousedici prvky, dokud nejsou ve spravnem poradi)
def bubbleSort(seznam):
    for i in range(len(seznam)):             # Vnejsi cyklus pres vsechny prvky seznamu
        setrideno = True                     # Pomocna promenna pro ukonceni cyklu1
        for j in range(len(seznam)-1-i):     # Poslednich i prvku uz je ve spravnem poradi
            if seznam[j] > seznam[j+1]:      # Pokud je j-ty prvek vetsi nez (j+1)-ty, budeme prohazovat
                seznam[j], seznam[j+1] = seznam[j+1], seznam[j]
                setrideno = False
        if setrideno:                        # Pokud uz je vse setrizeno, ukoncim cyklus
            break
    return seznam
