def sudaCisla_pocet(seznam):
	pocet = 0
	for prvek in seznam:
		if prvek%2 == 0:
			pocet += 1
	return pocet

def sudaCisla_vypis(seznam):
	seznamSuda = []
	for prvek in seznam:
		if prvek%2 == 0:
			seznamSuda.append(prvek)
	return seznamSuda


poleCisel = [1, 23, 20, 5, 6, 8]

print("Zadany seznam: ", poleCisel)
print("Pocet sudych cisel v seznamu je ", sudaCisla_pocet(poleCisel))
print("Suda cisla v seznamu: ", sudaCisla_vypis(poleCisel))
