"""
Generovani hodu kostkou
"""
import random

nHod = int(input("Zadejte pocet hodu: "))
pocty = [0]*6

for i in range(nHod):
    pocty[random.randint(0,5)] += 1

zastoupeni = [i/sum(pocty) for i in pocty]
print(pocty)
print(zastoupeni)