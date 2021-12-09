'''
You might find the function bin() useful.
Will be tested with n a strictly positive integer.
'''

import sys


def f(n):
    '''
    >>> f(1)
    1 in binary reads as: 1.
    Only one bit is set to 1 in the binary representation of 1.
    >>> f(2)
    2 in binary reads as: 10.
    Only one bit is set to 1 in the binary representation of 2.
    >>> f(3)
    3 in binary reads as: 11.
    2 bits are set to 1 in the binary representation of 3.
    >>> f(7)
    7 in binary reads as: 111.
    3 bits are set to 1 in the binary representation of 7.
    >>> f(2314)
    2314 in binary reads as: 100100001010.
    4 bits are set to 1 in the binary representation of 2314.
    >>> f(9871)
    9871 in binary reads as: 10011010001111.
    8 bits are set to 1 in the binary representation of 9871.
    '''
    a1=bin(n)
    a2=str(a1[2:])
    a3=0
    for i in range(len(a2)):
        if a2[i]=='1':
            a3+=1
    if a3==1:
        print(f'{n} in binary reads as: {a2}.\nOnly one bit is set to 1 in the binary representation of {n}.')
    if a3>1:
        print(f'{n} in binary reads as: {a2}.\n{a3} bits are set to 1 in the binary representation of {n}.')
    # Insert your code here


if __name__ == '__main__':
    import doctest
    doctest.testmod()
