"""Import random function
Create a function random_list_summer creates n elemented list with min value = -100 max value = 100 it has to print the list first and sum all the elements of it default element number is 15
Don't forget to call the function
for some features and functions you might have to search on the internet do it don't lose your courage"""

import random 

def random_list_summer():
    lista = []
    for i in range(15):
        lista.append(random.randint(-100, 100))

    print(lista) 
    somma = sum(lista)   
    print(somma)
random_list_summer()