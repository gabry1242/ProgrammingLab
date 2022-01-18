class ExamException(Exception):
    
    pass

class Diff():

    def __init__(self,ratio=1):
        
        if type(ratio) not in [int, float]:
            raise ExamException('passa un intero')
        
        if ratio < 1:
            raise ExamException('non posso dividere per 0 o un negativo')
        
        self.ratio=ratio
        
    def compute(self, lista):
        
        if type(lista) != list:
            raise ExamException('la lista deve essere una lista')

        
        lunghezza=len(lista)

        if lunghezza < 2:
            raise ExamException('la lista deve avere elementi')


        if type(lunghezza) != int:
            raise ExamException('devi passare un intero')
            
        for i in range(lunghezza):

            if type(lista[i]) not in [int, float]:
                raise ExamException('la lista deve avere solo interi')
        
        output=[]

        for i in range(lunghezza-1):

            differenza=0
            
            
            differenza=lista[i+1]-lista[i]

            
            risultato=differenza/self.ratio

            output.append(risultato)
        
        return output


