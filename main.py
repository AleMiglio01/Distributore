from model.Distributore import Distributore

distributore = Distributore()

distributore.aggiungiBevanda("Acqua","1",0.30)
distributore.aggiungiBevanda("Thé","2",0.40)
distributore.aggiungiBevanda("Fanta","3",1.20)

distributore.getPrice("1")
print("Il prezzo della bevanda è: ", distributore.getPrice("1"))

distributore.getNome("2")
print("Bevanda in posizione indicata: ", distributore.getNome("2"))

distributore.caricaTessera(15, 6.4)
distributore.caricaTessera(16, 11.0)
distributore.caricaTessera(17, 1.40)

distributore.leggiCredito(16)
print("Credito tessera indicata: ", distributore.leggiCredito(16))

distributore.aggiornaColonna("Acqua",20)
distributore.aggiornaColonna("Thè",8)
distributore.aggiornaColonna("Fanta",30)

distributore.erogaBibita("1",17)