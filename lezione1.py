#definisco la funzione somma
def somma(lista):
    #inizializzo il risultato
    risultato=0
    #leggi ciascun elemento e sommalo
    for item in my_list:
        risultato=risultato+item
    return risultato
#inserisco la mia lista
my_list=[1, 4, 78, 43, 92, 143]
#leggere tutti gli elementi della lista e sommarli 
print (somma(my_list))