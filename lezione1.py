#definisco la funzione somma
def somma(lista):
    #inizializzo il risultato
    risultato=0
    for item in my_list:
        risultato=risultato+item
    return risultato

my_list=[1, 4, 78, 43, 92, 143]
#leggere tutti gli elementi della lista e sommarli 
print (somma(my_list))