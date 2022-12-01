def mocnina(seznam):
    return [i*i for i in seznam]

def suda(seznam):
    return [i for i in seznam if i%2==0]

def prunik(s1, s2):
    return [i for i in s1 if i in s2]
    # Reseni pres vyuziti mnozin (budeme brat priste),
    # pokud se prvky mohou opakovat
    #return list(i for i in set(s1) if i in set(s2))

def palindrom(text):
    return [i for i in text.split() if i == i[::-1]]

def skalSoucin(v1, v2):
    return sum([i*j for i, j in zip(v1, v2)])

if __name__ == '__main__':
    print(skalSoucin([1, 2, 3],[10, 20, 30]))
    print(prunik([1, 2, 3, 4, 5], [1, 4, 6, 8, 10]))
