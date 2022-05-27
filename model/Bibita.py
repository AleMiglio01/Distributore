class Bibita:
    def __init__(self, nome, codice, prezzo, distributore):
        self.nome = nome
        self.codice = codice
        self.prezzo = prezzo
        self.distributore = distributore
    def strPrice(self):
        str = self.nome +" "+ self.codice +" "+ self.prezzo
        return str