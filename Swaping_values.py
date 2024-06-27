# swapping values
a=int(input('enter a value='))
b=int(input('enter b value='))
print(f'Before swapping values are{a,b}')
a,b=b,a
print(f'After swapping values are{a,b}')
'''
output as follows 
enter a value=10
enter b value=20
Before swapping values are(10, 20)
After swapping values are(20, 10)
'''