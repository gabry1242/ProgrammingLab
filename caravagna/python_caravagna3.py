class Studente:

    ruolo = 'studente "Units"'

    def __init__(self,nome,cognome):

        self.nome=nome
        self.cognome=cognome
    
    def bonjour(self):
        print(self.ruolo, ":", self.nome, self.cognome)


obj_Gabriele= Studente("Gabriele", "Gianuzzo")

obj_Gabriele.bonjour()

