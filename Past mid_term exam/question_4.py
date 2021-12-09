'''
Will be tested with a at equal equal to 2 and b at most equal to 10_000_000.
'''
    

import sys
from math import sqrt


def f(a, b):
    '''
    >>> f(2, 2)
    There is a unique prime number between 2 and 2.
    >>> f(2, 3)
    There are 2 prime numbers between 2 and 3.
    >>> f(2, 5)
    There are 3 prime numbers between 2 and 5.
    >>> f(4, 4)
    There is no prime number between 4 and 4.
    >>> f(14, 16)
    There is no prime number between 14 and 16.
    >>> f(3, 20)
    There are 7 prime numbers between 3 and 20.
    >>> f(100, 800)
    There are 114 prime numbers between 100 and 800.
    >>> f(123, 456789)
    There are 38194 prime numbers between 123 and 456789.
    '''
    number_of_primes_at_most_equal_to_b = 0
    number = 0
    for i in range(a, b+1):
        if b == 2 or i == 2:
            number += 1
            flag = False
        else:
            flag = False
        for j in range(2, round(sqrt(i))+1):
            if i % j == 0:
                flag = False
                break
            else:
                flag = True
        if flag:
            number += 1
    number_of_primes_at_most_equal_to_b = number
    # Insert your code here
    if not number_of_primes_at_most_equal_to_b:
        print(f'There is no prime number between {a} and {b}.')
    elif number_of_primes_at_most_equal_to_b == 1:
        print(f'There is a unique prime number between {a} and {b}.')
    else:
        print(f'There are {number_of_primes_at_most_equal_to_b} prime numbers between {a} and {b}.')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
