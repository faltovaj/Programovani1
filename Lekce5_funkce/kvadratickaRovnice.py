import math
def kvadratickaRovnice(a, b, c):
    print("Reseni kvadraticke rovnice s temito parametry: a = ", a, ", b = ", b, ", c = ", c)
    if a == 0:
        print("Nejedna se o kvadratickou rovnici!")
        return []
    D = b**2 - 4*a*c
    koreny = []
    if D == 0:
        print("Rovnice ma jeden koren.")
        return [-b/2*a]
    elif D < 0:
        print("Rovnice nema reseni na mnozine realnych cisel.")
        return []
    else:
        x1 = (-b+math.sqrt(D))/2*a
        x2 = (-b-math.sqrt(D))/2*a
        print("Rovnice ma dva koreny.")
        return([x1,x2])

# Příklady:
print(kvadratickaRovnice(4, 0, -64))   # 2 kořeny
print()
print(kvadratickaRovnice(4, 0, 64))    # žádný kořen
print()
print(kvadratickaRovnice(1, -2, 1))    # 1 kořen




