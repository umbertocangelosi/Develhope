"""# Functions - Exercise 7 🐍

Create a lambda function that returns 2nd power of given number if its even   
and run it on the given list   
then print the result to the screen """

my_list= [*range(5)] 
print(my_list)
list_of_power=list(map(lambda i : i**2 if i % 2==0 else None,my_list))
print(list_of_power)

