from model.Bibita import Bibita
from model.Tessera import Tessera
from model.Colonna import Colonna

class Distributore:
    def __init__(self):
         self.tessere = []
         self.bibita_list = []
         self.credito_list = []
         self.colonna_list = []

    def aggiungiBevanda(self, nome, codice, prezzo):
        add_bevanda = Bibita(nome, codice, prezzo, self)
        self.bibita_list.append(add_bevanda)
        print(" ")
        print("codice: {}, nome: {}, prezzo {}".format(codice, nome, prezzo))
        found = "yes"

    def getPrice(self, codiceBibita):
        for bevanda in self.bibita_list:
            if bevanda.codice == codiceBibita:
             return bevanda.prezzo

    def getNome(self, codiceBibita):
        for bevanda in self.bibita_list:
            if bevanda.codice == codiceBibita:
                return bevanda.nome

    def caricaTessera(self, codiceTessera, credito):
        tessera = Tessera(codiceTessera, credito)
        self.tessere.append(tessera)
        print("Codice tessera: ", codiceTessera,"Credito caricato: ", credito)

    def leggiCredito(self, codiceTessera):
        for tessera in self.tessere:
            if tessera.codice == codiceTessera:
                return tessera.credito

    def aggiornaColonna(self, nomeBibita, numeroLattine):
        aggColonna = Colonna(nomeBibita, numeroLattine)
        self.colonna_list.append(aggColonna)
        print("Nome bibita:", nomeBibita,"/ Numero lattine aggiornato:", str(numeroLattine))

    def erogaBibita(self, codiceBibita, codiceTessera):
        prezzo = self.getPrice(codiceBibita)
        credito = self.leggiCredito(codiceTessera)
        nome = self.getNome(codiceBibita)
        if credito >= prezzo:
            for colonna in self.colonna_list:
                if colonna.numeroLattine >= 1 and colonna.nomeBibita == nome:
                    colonna.numeroLattine = colonna.numeroLattine - 1
                    break
            print("Nome bibita: {} Lattine rimaste: {}".format(colonna.nomeBibita, colonna.numeroLattine))
            for credits in self.tessere:
                if credits.codice == codiceTessera:
                    credits.credito = credits.credito - prezzo
            print("Codice Tessera: {} Credito residuo: {}".format(codiceTessera, credits.credito))