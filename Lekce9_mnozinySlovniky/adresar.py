#!/usr/bin/env python3
# Adresar kontaktu: vyhledavani, pridani a odebrani polozky

# Datovy typ: Seznam slovniku
mujAdresar = [
{
   'jmeno': 'Jana',
   'prijmeni': 'Faltova',
   'telefon': [123456789, 222956781],
   'adresa': { 'ulice': 'Kopecna',
               'cislo': 8,
               'mesto': 'Zdar nad Sazavou',
               'psc': 59103
               }
},
{
   'jmeno': 'Jan',
   'prijmeni': 'Novak',
   'telefon': [608608608],
   'adresa': { 'ulice': 'Miskovicka',
               'cislo': 8,
               'mesto': 'Praha',
               'psc': 19000
               }
},
{
   'jmeno': 'Daniel',
   'prijmeni': 'Fejt',
   'telefon': [],
   'adresa': { 'ulice': 'Benesova',
               'cislo': 8,
               'mesto': 'Hradec Kralove',
               'psc': 50002
               }
}
]

# Vyhledavani informaci o kontaktu
def vyhledejKontakt(jmeno, verbose = False):
    for i in range(len(mujAdresar)):
        kontakt = mujAdresar[i]
        if kontakt['prijmeni'] == jmeno:
            if verbose:
                print('Informace pro kontakt', jmeno)
                print('telefon:', kontakt['telefon'])
                print('ulice:', kontakt['adresa']['ulice'])
            return i
    print('Kontakt', jmeno, 'neexistuje.')
    return None

# Pridani noveho kontaktu do seznamu
def pridejKontakt(kontakt):
    if vyhledejKontakt(kontakt['prijmeni']) == None:
        print('Pridavame novy kontakt', kontakt['prijmeni'])
        mujAdresar.append(kontakt)
        print(mujAdresar[-1])
    else:
	    print('Kontakt uz existuje!')

# Odebrani kontaktu ze seznamu
def odeberKontakt(jmeno):
    if vyhledejKontakt(jmeno) == None:
        print('Kontakt', jmeno, 'neexistuje.')
        return
    else:
        print('Odebirame kontakt', jmeno)
        mujAdresar.pop(vyhledejKontakt(jmeno))
