abeceda ="""
A .−
B −...
C −. − .
D −..
E .
F .. − .
G −− .
H ....
I ..
J . − −−
K −.−
L . − ..
M −−
N −.
O −−−
P . − −.
Q − − .−
R . − .
S ...
T −
U ..−
V ...−
W . −−
X −..−
Y −. − −
Z − − ..
"""

def morseovka(slovo):
    # Pripravim si z retezce abeceda slovnik s pismeny jako klici
    # abecedu rozdelim podle jednotlivych radku
    ab = abeceda.split('\n')
    # Pripravim si prazdny slovnik
    slovnik = {}
    # Projdu seznam ab (jednotlive radky puvodniho retezce)
    for p in ab:
        # Zkontroluji, jestli neni polozka po odstraneni konce radku prazdna
        if len(p.strip())>1:
            # Rozdelim podle mezer
            pism = p.split()
            # Pismeno pouziji jako klic, sifru jako hodnotu
            slovnik[pism[0]] = pism[1]
            
    # A muzeme sifrovat: 
    for s in slovo:
        # Pismena si prevedu na kapitalky
        print(slovnik[s.upper()], end=' ')
    print()
