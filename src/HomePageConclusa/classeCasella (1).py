
class Casella:
    def init(self, id, statoCostruzione, personaggio):
        self.id = id
        self.statoCostruzione = statoCostruzione
        self.personaggio = personaggio

    def StampaCasella(casella):
        print ("Id Casella: " + casella.id)
        print ("Stato costruzione: " + casella.statoCostruzione)
        print ("Persanaggio: " + casella.personaggio)

    casella_00 = Casella(00, 1, "Costruttore")
    StampaCasella(casella_00)