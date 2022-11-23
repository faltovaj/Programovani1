#!/usr/bin/env python3
# Funkce na operace s retezci

# Fce otoci retezec
def otocRetezec(slovo):
    #return slovo[::-1]        # s vyuzitim rezu
    otoc =  []                  
    for i in range(1, len(slovo)+1):
        otoc.append(slovo[-i])
    return "".join(otoc)

# Fce otoci cislo
def otocCislo(cislo):
    return int(otocRetezec(str(cislo)))

# Fce spocita pocet slov
def pocetSlov(veta):
    return len(veta.split())

# Fce spocita pocet ruznych slov
def pocetRuznychSlov(veta):
    ruznaSlova = []
    for slovo in veta.split():
        if slovo.lower() not in ruznaSlova:
            ruznaSlova.append(slovo.lower())
    return len(ruznaSlova)

# Fce vyhodnotí výraz se sčítáním (vstup: 12+34+1, vystup: 47)
def scitani(vyraz):
    soucet = 0
    for cislo in vyraz.split('+'):
        soucet += int(cislo)
    return soucet

slovoTest = 'datel'
print(f"Otoc retezec: {slovoTest} na {otocRetezec(slovoTest)}")
cisloTest = 123456789
print(f"Otoc cislo: {cisloTest} na {otocCislo(cisloTest)}")
vetaTest = 'Mame radi Python, nebo ne?'
print(f"Pocet slov ve vete \"{vetaTest}\": {pocetSlov(vetaTest)}")
vetaTestOpakovani = 'Ruzna slova SLOVA ruzna mame radi Slova'
print(f"Pocet ruznych slov  ve vete \"{vetaTestOpakovani}\":{pocetRuznychSlov(vetaTestOpakovani)}")
vyrazNaScitani = '12+34+1'
print(f"Secti vyraz {vyrazNaScitani}: {scitani(vyrazNaScitani)}")
