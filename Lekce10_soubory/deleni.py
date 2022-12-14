def deleni(x, y):
    print(x/y)

def deleniTry(x, y):
    try:
        print(x/y)
    except:
        print('Chyba!!!!')

def deleniTry2(x, y):
    try:
        print(x/y)
    except ZeroDivisionError:
        print('Pozor: Deleni nulou!')
    except TypeError:
        print('Pozor: Nejsou zadana cisla!')

def deleniAssert(x, y):
    assert y != 0
    print(x/y)
