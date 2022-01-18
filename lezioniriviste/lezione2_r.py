#inizializzo lista vuota per salvare i valori
valori=[]
#apro il file in lettura
file=open('shampoo_sales.csv','r')
for line in file:
    elementi=line.split(',')

    if elementi[0]!='Date':
        
        numeri=elementi[1]
        valori.append(float(numeri))

file.close()

print(sum(valori))