"""# Classes and Objects - Exercise 3 🐍

Again let's keep talking on Animal class we have.  
with 3 methods we just reached the number of legs   
to prevent direct interactin with the class variables   
most of the other programming languages have encapsulation.  
But in python we don't have it 
instead we use `_` prefix for it as convention   
it is also same for the methods   
  
`_legs` this shows us not to touch this variable its up to you 
if you want to change it you can but `_`asks you politely not to do it. 

Change the `number_of_legs` to conventional private variable 
and call from another method

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