class CSVFile():
    def __init__(self, name):
        self.name=name
    
    def get_data(self):
        
        list=[]
        listoflist=[]
        try:
            file=open(self.name,'r')
        except:
            print('il nome del file è sbagliato mona')
        for line in file:
            #splitto gli elementi 
            elements= line.split(',')
            #faccio l'append degli elmenti alla lista
            if elements[0]!= 'Date':
                list.append(elements)
        
        file.close()

        listoflist.extend(list)
        return listoflist

class NumericalCSVFile(CSVFile):

    def get_data(self):

        string_data=super().get_data()

        numerical_data=[]
        
my_file= CSVFile(name='shampoo_sales.csv')
print('nome del file {}' .format(my_file.name))
print('Dati contenuti nel file {}' .format(my_file.get_data()))
