"""
Program vypise prirozena cisla od a do cisel zadanych uzivatelem (vcetne)
1/ pomoci for-cyklu
2/ pomoci while-cylku
"""

n_min = int(input("Zadejte spodni mez "))
n_max = int(input("Zadejte horni mez "))

print("=== Pomoci for-cyklu ===")
for i in range(n_min, n_max+1):
    print(i)

print("=== Pomoci while-cyklu ===")
cislo = n_min
while cislo <= n_max:
    print(cislo)
    cislo += 1        # cislo = cislo + 1
