"""# Classes and Objects - Exercise 1 🐍

Let's create Animal class and then create the 
animal object that runs and having 4 legs

create animal object with leg count 
when created print 
`"Animal object was created"`
and then call `runs` method of it and it prints 
`"Running started"` """

class animal():
    
    def __init__(self,n_leg):
        print('Animal object was created')
        self.n_leg=n_leg
        
    def runs(self):
        print('Running started')
        
    
cat=animal(4)
print(cat.n_leg)
cat.runs()