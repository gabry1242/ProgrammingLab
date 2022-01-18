#definisco una funzione che sommi gli elementi di una lista
def somma(lista):
    accumulatore=0
    for item in lista:
        accumulatore=accumulatore+item
    return accumulatore

#testo il programma su una liosta fatta da me
my_list=[1,2,3,4,5,6,7,8]

risultato=somma(my_list)

print(risultato)