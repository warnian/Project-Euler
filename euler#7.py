##CREATED 2/23/2016 by Ian Warn
##LAST EDITED 2/23/2016 by Ian Warn
"""
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


##check prime function from euler#3.py created 2/10/16
import math

def CheckPrime(primeNumber): ## function to check if number is prime returns bool
    Prime=True
    if primeNumber%2==0:         ## if number is even returns not prime
        Prime=False
        return Prime
        
    else:
        divisor=int(math.sqrt(primeNumber+1))
        for i in range(2,divisor+1):
           
            if primeNumber/i==primeNumber//i:
                Prime=False
                    
    return Prime     
##end CheckPrime Function
Prime_count=0
i=1
while Prime_count<10001:
    if CheckPrime(i)==True:
        
        Prime_count+=1
    i+=1

print(i-1)

##solved 2/23/2016
    
    

