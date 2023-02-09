"""Remember list,set,dictionary are mutable and tuple is 
immutable list,tuple elements can be reached by index
for dictionary it is not an option to reach by index the 
element key has to be known to reach and for set the items 
cannot be reached directly but it is possible to iterate."""

list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}

#print the lengths of list1,tuple1,set1,dict1
print(len(list1))
print(len(tuple1))
print(len(set1))
print(len(dict1))

#print the first element of list1 and tuple1
print(list1[0])
print(tuple1[0])

#print the value of lion key of dict1
print(dict1["lion"])

#change the 2nd position element of list1 to "rabbit"
list1[1]='rabbit'
print(list1[1])

#try to change the 2nd position element of the tuple to "rabbit" and explain what happened.
#tuple1[1]='rabit'is not possible because a tuple is immutable

#add "monkey" to list1
list1 = list1 + ['monkey']
print(list1)

#remove "rabbit" from list1
list1.remove('rabbit')
print(list1)

#in dict1 the number of feet is written as value to each animal the fixh has wrong value just fix it
dict1['fish']=0
print(dict1['fish'])
