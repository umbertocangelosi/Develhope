"""
# Classes and Objects - Exercise 4 🐍

Let's inherit Dog class from Animal 
add name(private) attribute to Dog class 
and then bark method to print `woof woof`

print name_of_dog 
make it bark`
count the legs 
"""
class animal():

    def __init__(self,n_leg):
        print('Animal object was created')
        self._n_leg=n_leg
        
    def runs(self):
        print('Running started')
    
    def legs_count(self):
        print(self._n_leg)

    def number_legs(self):
        return self._n_leg   
    

cat=animal(4)
print(cat._n_leg)
cat.runs()
print(cat.number_legs)

class Dog(animal):

    def __init__(self,n_leg,name):
        animal.__init__(self,n_leg)
        self._name=name

    def bark(self):
        print('woof woof')

dog=Dog(4,'Zara')

print(dog._name)
dog.bark()
dog.legs_count()