"""
Aproximace cisla pi pomoci nahodneho genaratoru
- Generujeme nahodne body ve ctverci [-1, 1] x [-1, 1]
- Uvnitr ctverce si predstavime jednotkovou vepsanou kruznici
- Myslenka: podil plochy kruhu a plochy ctverce je shodny s pomerem poctu
bodu uvnitr kruhu a celkovemu poctu generovanych pripadu
"""
import random as r
import math as m

n_celkem = 100000
n_kruh = 0

for i in range(n_celkem):
    x = r.uniform(-1,1)
    y = r.uniform(-1,1)
    if m.pow(x, 2) + m.pow(y,2) <= 1:
        n_kruh += 1
pi = 4*n_kruh/n_celkem
print(f'Cislo pi je priblizne {pi}.')
