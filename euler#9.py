##DATE CREATED 2/23/16 by Ian Warn
##LAST Edited 2/23/16 by Ian Warn
"""
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
condition=False
while condition==False:
    for i in range(1000):
        for j in range(1000):
                  
            if i*(i+j)==500:
                
                a=pow(i,2)-pow(j,2)
                b=2*i*j
                c=pow(i,2)+pow(j,2)
                condition=True

solution=a*b*c
print(a)
print(b)
print(c)
print(solution)
##Solved 2/23/16
