"""Compare those 2 numbers' absolute values and write X's absolute value greater than Y's absolute 
value Use abs function to do that
eg.
abs(-5) -> 5
abs function makes all numbers positive
"""
import random

number1 = random.randint(-100,100)
number2 = random.randint(-100,100)

if abs(number1) > abs(number2):
    print(f"{abs(number1)} is greater than {abs(number2)}")
elif abs(number2) > abs(number1):
    print(f"{abs(number2)} is greater than {abs(number1)}")    
else:
    print(f"{abs(number1)} equals to {abs(number2)}")
