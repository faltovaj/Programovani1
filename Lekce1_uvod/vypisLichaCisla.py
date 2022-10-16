# Program vypise licha cisla od 0 do zadaneho cisla
# Vstup: do jakeho cisla chcete vypisovat
# Vystup: vypis lichych cisel

nmax = int(input("Zadej, do jakeho cisla chces vypisovat: "))

for i in range(0,nmax+1):
    if i%2==1:
        print("Liche cislo: ", i)  
