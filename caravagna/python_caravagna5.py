class Veicolo:
    def __init__(self,p,v,km):
        self.posti=p
        self.velocita=v
        self.km=km
    
    
    

class Auto5(Veicolo):
    def __init__ (self,v,km):
        super().__init__("studente units", v, km)
        


giottero = Auto5("giottero", "gigi")

print(giottero.posti)
print(giottero.velocita)
print(giottero.km)