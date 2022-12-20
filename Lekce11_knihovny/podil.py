def deleni(x, y):
    try:
        print(x/y)
    except ZeroDivisionError:
        print('Pozor: Deleni nulou!')
