def factorial(n):
    if n<0:
        return 0
    else:
        fact=1
        for i in range(1,n+1):
            fact=fact*i 
    return fact
print(factorial(5))    


#recurcion
def recurcive_factorial(n):
    if n==1:
        return 1
    else:
        return n*recurcive_factorial(n-1)    


print(recurcive_factorial(5))





































