import sys
from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    up_bound = round(sqrt(n)) + 1
    for i in range(2, up_bound):
        if n % i == 0:
            return False
    return True

def f(a, b):
    '''
    The prime numbers between 2 and 12 (both included) are: 2, 3, 5, 7, 11
    The gaps between successive primes are: 0, 1, 1, 3.
    Hence the maximum gap is 3.
    
    Won't be tested for b greater than 10_000_000
    
    >>> f(3, 3)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 4)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 5)
    The maximum gap between successive prime numbers in that interval is 1
    >>> f(2, 12)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(5, 23)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(20, 106)
    The maximum gap between successive prime numbers in that interval is 7
    >>> f(31, 291)
    The maximum gap between successive prime numbers in that interval is 13
    '''
    if a <= 0 or b < a:
        sys.exit()
    max_gap = 0
    # Insert your code here
    
    list_of_prime = []

    for i in range(a, b + 1):
        if is_prime(i):
            list_of_prime.append(i)
    if len(list_of_prime) == 1 or len(list_of_prime) == 0:
        print('The maximum gap between successive prime numbers in that interval is 0')
    else:
        max_gap = list_of_prime[1] - list_of_prime[0]
        list_of_prime.sort()
        for i in range(len(list_of_prime) - 1):
            if list_of_prime[i+1] - list_of_prime[i] >= max_gap:
                max_gap = list_of_prime[i+1] - list_of_prime[i]
                max_gap -= 1
        print(f'The maximum gap between successive prime numbers in that interval is {max_gap}')

    
 #   print('The maximum gap between successive prime numbers in that interval is', max_gap)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
