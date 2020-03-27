

class Personaggio:
    def __init__(personaggio, nome, casella):
        personaggio.nome = nome
        personaggio.casella = casella

    def movimento(personaggio, casella):
        if personaggio.controlloMovimento(casella):
            personaggio.casella = casella
            return True
        else:
            return False


    def controlloMovimento (personaggio, casella) :
        ret= False
        if casella>=0 and casella <= 24:
            ret = (casella >= personaggio.casella - 6 and casella <= personaggio.casella - 3) or ret
            ret = (casella == personaggio.casella - 1) or ret
            ret = (casella == personaggio.casella + 1) or ret
            ret = (casella >= personaggio.casella + 3 and casella <= personaggio.casella + 6) or ret
        return ret

def main():
    p1 = Personaggio ("Bill", 6)
    swag = False
    swag = p1.movimento(9)
    print (p1.casella)


if __name__ == '__main__':
    main().run