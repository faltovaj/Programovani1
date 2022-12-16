def spocti(file):
    f = None
    while f is None:
        try:
            f = open(file, 'r')
        except:
            print('Soubor neexistuje, zadejte nazev jeste jednou: ')
            file = input()
    pocetRadku = 0
    pocetSlov = 0
    pocetZnaku = 0
    for line in f:
        line = line.strip()
        if (line != ""):
            pocetRadku += 1
            pocetSlov += len(line.split())
            pocetZnaku += sum([len(i) for i in line.split()])
    f.close()
    return pocetRadku, pocetSlov, pocetZnaku

def zkopiruj(fileIn, fileOut):
    with open(fileIn, 'r') as fin:
        with open(fileOut, 'w') as fout:
            for line in fin:
                fout.write(line)

def cisla(fileIn, fileOut):
    with open(fileIn, 'r') as fin:
        with open(fileOut, 'w') as fout:
            for line in fin:
                cisla = [i for i in line.split() if i.isdigit()]
                fout.write(' '.join(cisla)+'\n')

if __name__ == '__main__':
    filename = input('Zadejte nazev souboru: ')
    print(spocti(filename))
    zkopiruj(filename, 'out.txt')
    cisla(filename,'outCisla.txt')