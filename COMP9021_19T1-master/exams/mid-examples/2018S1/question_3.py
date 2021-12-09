
from math import sqrt

def get_all_divisor(n):
    if n == 1:
        return [1]
    result = set([])


    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return result

def number_calculate(n,d):
    m = n
    count = 0
    while m!=0:
        m, a = divmod(m, d)
        if a == 0:
            count +=1
        else:
            break
    return count

def f(n, d):
    '''
    >>> f(2, 1)
    1 is not a proper factor of 2.
    >>> f(2, 2)
    2 is not a proper factor of 2.
    >>> f(16, 2)
    2 is a proper factor of 16 of mutiplicity 4.
    >>> f(100, 20)
    20 is a proper factor of 100 of mutiplicity 1.
    >>> f(8 ** 7 * 3 ** 5 * 11 ** 2, 8)
    8 is a proper factor of 61662560256 of mutiplicity 7.
    >>> f(3 ** 3 * 11 * 13 ** 2 * 40 ** 6, 8)
    8 is a proper factor of 205590528000000 of mutiplicity 6.
    '''

    if d == 1 or n == d:
        print(f"{d} is not a proper factor of {n}.")
    else:
        count = number_calculate(n,d)
        if count > 0:
            print(f"{d} is a proper factor of {n} of mutiplicity {count}.")



if __name__ == '__main__':
    import doctest
    doctest.testmod()
