class Tessera():
    def __init__(self, codice, credito):
        self.codice = codice
        self.credito = credito

    def descrizioneTessera(self):
        descrizione = "Codice: " + self.codice + "Credito" + self.credito
        return descrizione

    def getCodiceTessera(self, codice):
        self.codice = codice
        return codice

    def getCredito(self, codice):
        return self.credito