"""
Automat na mince: Program rozdeli zadanou castku na mince (50, 20, 10, 5, 2, 1).
Vstup: castka
Vystup: kolik kterych minci
"""

# Vstup
castka = int(input("Kolik chcete rozmenit? "))

# Postupnym delenim zjistime pocty minci
pocet50 = castka//50
castka = castka%50

pocet20 = castka//20
castka = castka%20

pocet10 = castka//10
castka = castka%10

pocet5 = castka//5
castka = castka%5

pocet2 = castka//2
castka = castka%2

pocet1 = castka

# Kontrola spravnosti vypoctu
kontrola = pocet50*50 + pocet20*20 + pocet10*10 + pocet5*5 + pocet2*2 + pocet1
print("Kontrola: ", kontrola)

print("Pocet 50-ti korun", pocet50)
print("Pocet 20-ti korun", pocet20)
print("Pocet 10-ti korun", pocet10)
print("Pocet 5-ti korun", pocet5)
print("Pocet 2 korun", pocet2)
print("Pocet 1 korun", pocet1)
