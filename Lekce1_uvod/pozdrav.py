# Program vypise pozdrav, nacte jmeno zadane z klavesnice

# Vypis na obrazkovku
print("Dobry den")
# Vstup z klavesnice
name = input('Jak se jmenujes? ')

# Pridame podminku
# Vstup: ocekavame ano/ne
pozdravit = input('Chcete pozdravit? ')

if pozdravit == "ano":
    print("Zdravim", name)
else:
    print('Hello world!')
