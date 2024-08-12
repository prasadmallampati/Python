'''
Day 3: Functions
    ●	Learning: Defining functions, arguments, return values.
    ●	Practice :
        ○	Write a function to calculate the factorial of a number.
        ○	Create a function to check if a string is a palindrome.
'''



# syntax
'''
def function_name(parameter):
    # block of code
    return value

'''

def greet():

    print("hello this is custom defind function...")


'''
Function Arguments
Arguments are values you can pass into functions when you call them. These values are used by the function to perform its task. Arguments are specified in the parentheses of the function definition.

Types of Arguments:

Positional Arguments: These are the most common. Their order matters.
Keyword Arguments: These are passed by explicitly naming each argument. Their order doesn't matter.
Default Arguments: These are arguments that assume a default value if not provided by the caller.
Arbitrary Arguments: Using *args for a tuple of arguments and **kwargs for a dictionary of keyword arguments.


'''


# 1 positional aruguments

'''
# syntax :
def function_name(arg1,arg2):
    block of code
    return statement

'''
def add(a,b):
    return a+b
add(110,33)



# 2  keyword aruguments
'''
# syntax

def function_name(arg1,arg2):
    block of code
    return statement

'''
def multiply(a,b):
    return a*b
multiply(a=12,b=2)



# 3 default aruguments
# means if not  passing any arg to default will executes else what ever we pass that will execute


'''
def function_name(arg1,arg2="value"):
    block of code
    return statement

'''
def greet(name,greeting="Hello"):
    
    return f"{greeting},{name}"

print(greet("prasad"))
print(greet('prasad','hi'))



# 4-1 arbitary arguments


'''

# syntax
def function_name(*args):
    # Code block
    return statement
'''

# example: -

def add_num(*args):
    return sum(args)

print(add_num(1,2,3,4,5))

# 4-2 **kwargs
'''
syntax :
def fucntion_name():
    block of code
    return statement
'''
# example display
def display(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')
print(display(name='prasad',age=20,dept='cse'))


'''
# position only arguments

def function_name(arg1, arg2, /, arg3, arg4):
    # Code block
    return value
'''

# example 

def pow(x, y, /, z=1):
    return (x ** y) * z

print(pow(2, 3)) 
print(pow(2, 3, z=4)) 


''''

keyword only arguments 

# syntax 
def function_name(arg1, arg2, *, arg3, arg4):
    # Code block
    return value


'''
# example

def introduce(name, age, *, city="Unknown", country="Unknown"):
    return f"{name} is {age} years old, from {city}, {country}."

print(introduce("prasad", 18, city="hyd", country="india"))

# practice 

# ○	Write a function to calculate the factorial of a number.


def fact(n):
    if n==0 or n==1:
        return 1
    else:
       return  n*fact(n-1)
for i in range(1,11):
    print(f"factorial {i} is {fact(i)}")
    
# ○	Create a function to check if a string is a palindrome.

def palindrome(s):
    
    res=''.join(char.lower() for char in  s if char.isalnum())
    
    return res==res[::-1]

print(palindrome('A man, a plan, a canal, Panama'))




# interview 
'''
5.	How do Python’s list comprehensions work?
6.	How does Python’s range function work with negative steps
'''
# syntax  for list comprehensions
 # [expression for item in iterable if condition]
 
# 5.How do Python’s list comprehensions work?
# example for list comprehesion
l=[i for i in range(10)  if i%2==0 ]
print(l)




# syntax for range function
# range(start,stop,step)

# How does Python’s range function work with negative steps
# example:

for i in range(10,0,-1):
    print(i)
    
