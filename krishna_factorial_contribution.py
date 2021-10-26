
import math

a=int(input())
b=math.factorial(a)
print ('a! =',b)


e=1
for d in range(a,1,-1):
    e=d*e
    
print ('a! =',e)


def fact(a):
    if a==0:
       return 1
    else:
        return a*fact(a-1)
        
f=fact(a)      
print ('a! =',f)

