# Nacti dve cisla a vypis to vetsi z nich
# Vstup: 1/ prvni cislo, 2/ druhe cislo

cislo1 = int(input("Zadej prvni cislo: "))
cislo2 = int(input("Zadej druhe cislo: "))

if cislo1>cislo2:
    print("Vetsi cislo je ", cislo1)
elif (cislo1==cislo2):
    print("Cisla jsou si rovna ", cislo1, cislo2)
else:
    print("Vetsi cislo je ", cislo2)
