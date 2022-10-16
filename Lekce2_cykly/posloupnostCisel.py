"""
Program ze vstupu nacte posloupnost prirozenych cisel. Cisla budou zadana kazde na samostatne
radce, vstup bude ukoncen cislem -1 (ta uz do posloupnosti nepatri).
- Vratte soucet teto rady
- Urcete prvni a druhe maximum (poznamka: definuji si 2. maximum z rady 3 4 4 jako cislo 4)
"""

print("Zadejte radu cisel oddelenych enter, ukonceni vstupu -1")
cislo = int(input())
suma = 0
max1 = 0    # Prvni nejvetsi cislo, puvodni hodnota 0
max2 = 0    # Druhe nejvetsi cislo, puvodni hodnota 0

while cislo != -1:
	suma += cislo
	if cislo >= max1: 
		max2 = max1
		max1 = cislo
	elif cislo >= max2:
		max2 = cislo
	cislo = int(input())

print("Soucet cisel je", suma)
print("Maximum je", max1)
