
class Studente:

    numeroStudenti = 0                       #variabile di classe condivisa in tutti gli oggetti di tipo Studente

    def __init__(self, nome, cognome, classe):         #costruttore (self sempre necessario)
        
        self.nome = nome
        self.cognome = cognome
        self.classe = classe
        Studente.numeroStudenti += 1

    def show(self):                                    #Metodo (self sempre necessario)
        print("Scheda Studente:")
        print("Nome: " + self.nome)
        print("Cognome: " + self.cognome)
        print("Classe: " + self.classe, end = "\n\n")


a = Studente("Alle", "Cristo", "Quinta")

b = Studente("Zip", "Lop", "Univerità")


a.show()
b.show()

print("Nell' istituto sono presenti " + str(Studente.numeroStudenti) + " studenti.")

