"""
Day 1: Python Basics
●	Learning (20 min): Variables, data types, and basic operations.
●	Practice (40 min):
○	Create variables for different data types (int, float, string).
○	Write a program to swap two numbers.
"""


'''

Q1  :What is variable ?
ans : variable which holds the value

Rules for Variables 
1. It should always starts with alphabets,alphanumaric and underscore
2. it does not starts with or special symbol


'''
# Create variables for different data types (int, float, string).

# method 1 create variable with values which is statical type

atm_withdraw_amount=2000

salary=39000.50

name_of_employee="prasad"





# method 2 create variable and read values in run time i.e dynamic
# here default input type is str which is string so we are converting one req type of values which is type casting


atm_withdraw_amount = int(input())

salary = float(input())

name_of_employee = str(input())





# method 3 reading values with type annotation in static way

atm_withdraw_amount: int = 2000.00

salary : float = 30000.00

name_of_employee :str = "prasad"



# method 4 reading number with type annotation in dynamically

atm_withdraw_amount : int =input()

salary : float =input()

name_of_employee : str=input()



a=20
b=2

while True:
        options=input('Enter options (add sub div mul):')
        
        if options == 'add' or options=='+': 
            print("Addition is a+b=",a+b)
            
        elif options== 'sub' or options=='-':
            print("sub is a-b=",a-b)
        
        elif options== 'mul' or options=='*':
            print("multipication is a*b=",a*b)
        
        elif options== 'div' or options=='/':
            print("divison is a/b=",a/b)
            
        else:
            print('option not available')
        





# Write a program to swap two numbers.
# swaping two number in the sence interchaning values

a=10
b=20

print("Before swaping")
print("A=",a,"B=",b)

a,b=b,a
print("after swaping")
print("A=",a,"B=",b)


# 6  Diffrence b/w == and is

x=10
y=10
print(x==y)



print(x is y)





