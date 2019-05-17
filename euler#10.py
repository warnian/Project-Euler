##CREATED 2/23/2016 by Ian Warn
##LAST EDITED 2/23/2016 by Ian Warn 
"""
Problem 10
Published on Friday, 8th February 2002, 06:00 pm; Solved by 203670; Difficulty rating: 5%
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

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

Prime_Sum=2
for i in range(2,10):
    if CheckPrime(i)==True:
        print(i)
        Prime_Sum+=i
   
print(Prime_Sum)

#solved 2/23/2016
