### Created 2/10/16
"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
### Last Edited by Ian Warn 2/10/16
total=0
divisible=False
for i in range(1,1000):
    if i//5 == i/5:
        divisible=True

    elif i//3 ==i/3:
        divisible=True

    if divisible==True:
        total+=i
        divisible=False

        i+=1

print(total)
        

        
            
