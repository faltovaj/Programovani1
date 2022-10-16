"""
Program spocita obvod a obsah obdelniku
Vstup: delka strany/stran
Vystup: obvod a obsah
"""

stranaA = float(input("Strana A: "))
stranaB = float(input("Strana B: "))
print("Obvod obdelnika: ", (stranaA+stranaB)*2)
print("Obsah obdelnika: ", stranaA*stranaB)
