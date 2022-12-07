predvolba = {
    1: ['mamka',123456789],
    2: 'tatka',
    3: 'babicka',
    4: 'Romca'
}
print(predvolba[1][1])


kontakt = {
'jmeno': 'Jana' ,
'prijmeni' : 'Faltova' ,
'telefon' : 222956781,
'adresa' : { 'ulice' : 'Kopecna' ,
'cislo' : 8,
'mesto' : 'Zdar n. Saz.',
'psc' : 59103,
}
}

print(kontakt['prijmeni'], ', ulice ', kontakt['adresa']['ulice'])


bludiste = {
    (1, 1): 'X',
    (2, 3): 'X',
    (8, 8): 'X'
}
ndim = 10
for i in range(ndim):
    for j in range(ndim):
        if (i,j) in bludiste:
            print(bludiste[(i,j)], end=" ")
        else:
            print('.', end=" ")
    print()

# Prevedte si abecedu do tvaru s vyuzitim prace s retezci: mors = {'A': '.-', ATD.}
abeceda = """
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

