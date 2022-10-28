#!/usr/bin/env python3
# Program otestuje, zda je zadane cislo prvocislem

cislo = int(input("Zadejte cislo "))

"""
# 1/ pomoci for cyklu s pomocnou promennou
mamDelitele = False
for i in range(2, cislo):
    if cislo%i == 0:
        print("Cislo ", cislo, "neni prvocislo")
        mamDelitele = True
        break
if not mamDelitele:       # ekvivalentni s mamDelitele == False
    print("Cislo ", cislo, "je prvocislo")
"""

# 2/ pomoci while-else (neni nutna pomocna promenna)      
i = 2
while i*i <= cislo:
    if cislo%i == 0:
        print("Cislo ", cislo, "neni prvocislo")
        break
    i += 1
else:
     print("Cislo ", cislo, "je prvocislo")
