"""
Permutace od 1 do N - urcete pocty pevnych bodu
Pevny bod: Zobrazi se sam na sebe
"""
import random as r

N = int(input("Zadejte cislo N: "))
Npokusu = 1000
bezPevnehoBodu = 0
for i in range(Npokusu):
    pevnyBod = 0
    perm = r.sample(range(N), k = N)
    for j in range(len(perm)):
        if j == perm[j]:
            pevnyBod += 1
    if pevnyBod == 0:
        bezPevnehoBodu += 1

print(f'Pravdepodobnost zadneho pevneho bodu je {bezPevnehoBodu/Npokusu*100}%.')