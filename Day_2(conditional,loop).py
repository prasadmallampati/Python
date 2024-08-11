
'''
                                            Day 2: Control Structures
Learning : If-else statements, loops (for, while).

'''

# if syntax
'''
if condition:
    condition true case if inside block of code execute
else:
    condition false case else will execute

'''
# if example
age=int(input())

if age>18: 
    print('Your eligible for voting or marriage and other activities')
else:
    print(f'wait for {18-age} year for casting vote or marriage or other activitess') 


#loop in python they are two for and while
# for is used for iteration untill condition met
# while is used for both iteration and condition also


# for syntax

'''
for item in seq:
    block of code inside for

'''


# for example for range of numbers

for i in range(5):
    print(i)



# while syntax

'''
while condition:

    block of code inside while
'''

# while example


count=0
while count< 5:
    print(count)
    count+=1
else:
    print('end of loop')
    
    
    
# infinite loop

while True:
    print('running......') # execution not possible to stop untill we end loop or break the loop or ctrl+c


'''
Practice :
Write a program to find the largest of three numbers.
Create a loop to print the first 10 Fibonacci numbers

'''
# largest of three numbers 

a=eval(input())
b=eval(input())
c=eval(input())

if a>=b and a>=c:
    largest_value=a
elif b>=a and b>=c:
    largest_value=b
else:
    largest_value=c
print(largest_value)


# fibonacci numbers

a,b=0,1
print("first 10 fibonacci numbers")

for i in range(10):
    print(a)
    # a values is b, b is a+b 
    
    a,b=b,a+b

'''
            Interview 
3.	Can you explain what the pass statement does?
4.	What is the difference between a list and a tuple?
'''

'''

pass is used for place holder
pass is used for condition not met perpose



'''

# examples for pass

class Person:
    
    pass




def myfun():
    
    pass


for i in range(10):
    
    pass



if age>18:
    pass




# 4 list and tuple


l=[1,2,3,4,5]


print(l)


# used for adding value into list

l.append(6)

print(l)

# also used for delete element in list
l.remove(4)

print(l)


# used for pop the element means delete from list
l.pop(0)


print(l)


# using  for order
l.sort()

print(l)



# tuple



t=('prasad','hello')


print(t.count('prasad'))

print(t.index('hello'))
