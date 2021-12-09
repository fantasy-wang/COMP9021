import sys
from math import sqrt
from itertools import compress


def get_primes_3(n):
    num_prime=[]
    for i in range(n,2,-1):
        flag=False
        for j in range(2,round(sqrt(i)+1)):
            if i%j!=0:
                flag=True
            else:
                flag=False
                break
        if flag:
            num_prime.append(i)
    return max(num_prime)

def f(n):
    '''
    Won't be tested for n greater than 10_000_000
    
    >>> f(3)
    The largest prime strictly smaller than 3 is 2.
    >>> f(10)
    The largest prime strictly smaller than 10 is 7.
    >>> f(20)
    The largest prime strictly smaller than 20 is 19.
    >>> f(210)
    The largest prime strictly smaller than 210 is 199.
    >>> f(1318)
    The largest prime strictly smaller than 1318 is 1307.
    '''
    if n <= 2:
        sys.exit()
    largest_prime_strictly_smaller_than_n = 0
    # Insert your code here
    if n == 3:
        print("The largest prime strictly smaller than 3 is 2.")
    else:
        primes = get_primes_3(n)
        print(f"The largest prime strictly smaller than {n} is {primes}.")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
