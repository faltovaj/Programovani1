"""
Prevody jednotek: Prevedte delku v m na mm, cm nebo dm (podle prani uzivatele)
Vstup: delka v m; jednotky, na ktere chceme prevadet
Vystup: delka v pozadovanych jednotkach
"""

# Prvni vstup: musime pretypovat na cele cislo (int)
delka = int(input("Zadejte delku v m "))
# Druhy vstup: jednotky
jednotka = input("Na jakou jednotku chcete prevadet? ")

# Prevody a vypis
if jednotka == "mm":
    print("Delka v mm je", delka*1000)
if jednotka == 'cm':
    print("Delka v cm je", delka*100)
if jednotka == 'dm':
    print("Delka v dm je", delka*10)
