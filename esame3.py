class ExamException(Exception):

        pass

class MovingAverage():

    def __init__(self, length):
        
        if type(length) != int:
            raise ExamException('Errore le medie mobili devono essere di interi')
        
        if length < 1:
            raise ExamException('Errore non posso dividere per zero')
       
        self.length=length

        
    def compute(self,lista):
        
        if type(lista) != list:
            raise ExamException('errore')
        lunghezza=len(lista)
        if lunghezza==0:
            raise ExamException('Errore la lista non ha elementi')
        
        if self.length>lunghezza:
            raise ExamException ('errore')
    
        if type(lunghezza) != int:
            raise ExamException('Errore le medie mobili devono essere di interi')
        
        lista_ritorno=[]
    
        for i in range(lunghezza-self.length+1):
            
            p=i

            somma=0

            for e in range(self.length):

                
                
                if type(lista[p]) not in [int, float]:
                    raise ExamException('Errore la lista deve contenere interi')
                somma=somma+lista[p]
                if type(somma) not in [int, float]:
                    raise ExamException('Errore la somma di numeri deve essere un intero o un float')
                p=p+1

            risultato=somma/self.length
            lista_ritorno.append(risultato)

        
        return lista_ritorno
        


    
moving_average = MovingAverage(2)


result = moving_average.compute([2,4,8,16])


print(result) # Deve stampare a schermo [3,6,12]    