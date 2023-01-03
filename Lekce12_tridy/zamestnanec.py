class Zamestnanec:
    """ Trida k evidenci zamestnancu """
    def __init__(self, jmeno, prijmeni, pracoviste):
        """ Initializace jmena, prijmeni a pracoviste zamestnance """
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.pracoviste = pracoviste

    def vrat_email(self):
        """ Funkce vrati email zamestnance """
        return self.jmeno + '.' + self.prijmeni + '@mff.cuni.cz'

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}, {self.pracoviste}'

    def __eq__(self, other):
        """ Definice rovnosti instanci self a other """
        return self.jmeno == other.jmeno and \
            self.prijmeni == other.prijmeni

help(Zamestnanec)