#esempio pratico
#funzioni algebriche    
#dichiarare la classe figura e inizializzare permietro e area
from abc import ABC, abstractmethod
from math import pi
class Figura(ABC):
    @abstractmethod
    def permietro(self):
        pass
    
    @abstractmethod
    def area(self):
        pass

class Triangolo(Figura):

    def __init__(self,a,b,c,h):
        self.a=a
        self.b=b
        self.c=c
        self.h=h

    def permietro(self):
        return self.a+self.b+self.c

    def area(self):
        return self.b*self.h/2


t=Triangolo(3,4,5,4)
print(t.area())
    

class Circonferenza(Figura):
    def __init__(self,r):
        self.r=r
    
    def permietro(self):
        return self.r*2*pi
    
    def area(self):
        return pi*self.r**2
