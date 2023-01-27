"""to convert a number to string we can use str() function this is called casting

cast num1 to string and assign to num1_str
check the length of the string
get the third element of string (the one in the 3rd order)
get the 3-5 elements of string (both inclusive) by string slicing
check if num2 in string (cast if necessary)
check if num3 in string (cast if necessary)
concatenate 0 to the string from left and assign to string_with_0
get the characters of string_with_0 from start to position 4 (end point exclusive)
get the characters of string_with_0 from position 5 until the end
use negative indexing to reach the "567" string_with_0"""

num1 = 1122334455666 
num1_str = str(num1)
print(len(num1_str))
num2 = num1_str[2] 
print(num2)
num3 = num1_str[2:5]
print(num3)

if num2 == str:
    print(f'is already a {type(num2)}')
else:
    num2 = str(num2)
    print(f'now after casting is a {type(num2)}')

if num3 == str:
    print(f'is already a {type(num3)}')
else:
    num3 = str(num3)
    print(f'now after casting is a {type(num3)}')

string_with_0 = f'0{num1}'
print(string_with_0)

print(f'{string_with_0[:4]}!')

print(string_with_0[4:])



    

