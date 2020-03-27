
class Casella:
    def __init__(self, id, statoCostruzione, personaggio):
        self.id = id
        self.statoCostruzione = statoCostruzione
        self.personaggio = personaggio

    def StampaCasella(self):
        print ('Id Casella: ' + str(self.id))
        print ('Stato costruzione: ' + str(self.statoCostruzione))
        print ('Persanaggio: ' + self.personaggio)

casella_1 = Casella(1, 1, 'Costruttore')
casella_1.StampaCasella()