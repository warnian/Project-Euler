## Date Created 2/10/16 by Ian Warn
'''
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number  600851475143?
'''

##Last Edited 2/10/16


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

def oddFactors(number): ##function to find factors of a number
    Factors_list=list()
    divisor=int(number/2)
    
    for i in range(1,divisor+1,2):
        
        if number/i ==number//i:
            Factors_list.append(i)
            
    return Factors_list
##end Factors Function

PrimeFactors=list()
for element in oddFactors(600851475143):
    ##print(element)
    if CheckPrime(element)==True:
        
    
        PrimeFactors.append(element)

##print(PrimeFactors)
print(PrimeFactors)
maximum=PrimeFactors.pop()
print(maximum)



"""for element in Factors(600851475143):
    if CheckPrime(element)==True:
        PrimeFactors.append(element)
"""

        
        
            


    
