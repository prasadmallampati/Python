#factorial program
def fact(n):
  if n==1 or n==0:
    return 1
  else:
    return n*fact(n-1)
n=int(input('Enter n value='))
fact(n) # calling function
'''
output as follows 
Enter n value=5
120
'''