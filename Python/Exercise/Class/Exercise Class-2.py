"""# Classes and Objects - Exercise 2 🐍

Now continue with the Animal class we had used before 

Add a method to count the legs `count_legs`
which prints the number of legs 

Add a method to count the legs `return_legs`
which returns the number of legs 

print number of legs directly from  `number_of_legs` 
variable of the object 
"""

class animal():

    def __init__(self,n_leg):
        print('Animal object was created')
        self.n_leg=n_leg
        
    def runs(self):
        print('Running started')
    
    def legs_count(self):
        print(n_leg)

    def number_legs(self):
        return self.n_leg   
    
cat=animal(4)
print(cat.n_leg)
cat.runs()
print(cat.number_legs)