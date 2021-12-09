import math

def all_prime(n):
    list1=[]
    for i in range(2,n+1):
        if isprime(i):
            list1.append(i)
    return list1


def isprime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


print(all_prime(1000))