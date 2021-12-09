import sys
from math import sqrt

def f(a, b):
    '''
    Won't be tested for b greater than 10_000_000
    
    >>> f(3, 3)
    The number of prime numbers between 3 and 3 included is 1
    >>> f(4, 4)
    The number of prime numbers between 4 and 4 included is 0
    >>> f(2, 5)
    The number of prime numbers between 2 and 5 included is 3
    >>> f(2, 10)
    The number of prime numbers between 2 and 10 included is 4
    >>> f(2, 11)
    The number of prime numbers between 2 and 11 included is 5
    >>> f(1234, 567890)
    The number of prime numbers between 1234 and 567890 included is 46457
    >>> f(89, 5678901)
    The number of prime numbers between 89 and 5678901 included is 392201
    >>> f(89, 5678901)
    The number of prime numbers between 89 and 5678901 included is 392201
    '''
    sieve = list(range(2, b + 1))
    i=0
    while sieve[i] <= round(sqrt(b)):
        sieve_as_set = set(sieve) 
        k=0
        while True:
            factor = sieve[i] * sieve[i + k]
            if factor > b:
                break
            sieve_as_set.remove(factor)
            k+= 1
        sieve = sorted(sieve_as_set)
        i+= 1
    i = 0
    for e in sieve:
        if e >=a:
            break
        i+=1
    sieve = sieve[i:]
    length = len(sieve)
    print(f'The number of prime numbers between {a} and {b} included is {length}')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
