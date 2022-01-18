#creare una lista
valori=[]
#apro e leggo il file txt
lista=open('shampoo_sales.csv','r')

#divido gli elementi per prendere i valori e non le date
for line in lista:
    oggetto=line.split(',')

    if oggetto[1]!='Sales\n':
        
        valori.append(float(oggetto[1]))


#sommao tutti i valori
listsum=sum(valori)
print(listsum)