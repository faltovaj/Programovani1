#!/usr/bin/env python3
# Program vypise vsechna prvocisla od 2 do zadaneho cisla

maxn = int(input("Zadejte cislo "))

cislo = 2
while cislo <= maxn:
    delitel = 2
    while delitel*delitel <= cislo:
        if cislo%delitel == 0:
            break
        delitel += 1
    else:
        print(cislo)
    cislo += 1
