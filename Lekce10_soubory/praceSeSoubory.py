# Ukazka prace se soubory

f = open('soubor.txt','r')    # otevreni souboru ke cteni ('r')
obsah = f.read()              # nacteni obsahu celeho souboru
f.close()

# Vypiseme obsah souboru
print(obsah)

# Dalsi moznost
with open('soubor.txt', 'r') as f:
    # cteni souboru po radcich
    for line in f:
        print(line)
        #print(line.strip())    # Odstraneni bilych znaku na zacatku ci na konci retezce
        #print(line.split())    # Vyzkousejte split(" ")
