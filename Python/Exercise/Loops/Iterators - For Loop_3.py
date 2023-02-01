"""Iterate each elements of list1,tuple1,set1 and print them out
For the dict1 iterate all elements but only print the ones who are living on land in the form of x lives in y"""

list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

for c,elemento in enumerate(list1):
    print(elemento)

print()

for c,elemento in enumerate(tuple1):
    print(c,elemento) 

print()

for elemento in set1:  #set is not a iterable class 
    print(elemento)     

print()

for elemento in dict1:
    if dict1[elemento] == 'land':
        print(f'{elemento} lives in {dict1[elemento]}' )