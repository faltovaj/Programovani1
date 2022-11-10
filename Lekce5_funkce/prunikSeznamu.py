def prunik_seznamu(seznam1, seznam2):
    seznam_prunik = []
    i1, i2 = 0, 0
    while i1 != len(seznam1) or i2 != len(seznam2):
        if seznam1[i1] == seznam2[i2]:
            seznam_prunik.append(seznam1[i1])
            i1 += 1
            i2 += 1
        elif seznam1[i1] < seznam2[i2]:
            i1 += 1
        else:
            i2 += 1
    return seznam_prunik

cisla1 = [6, 7, 8, 9, 10, 11, 12]
cisla2 = [1, 5, 6, 7, 12]
print("Prvni serazeny seznam: ", cisla1)
print("Druhy serazeny seznam: ", cisla2)
print("Prunik seznamu: ", prunik_seznamu(cisla1, cisla2))
