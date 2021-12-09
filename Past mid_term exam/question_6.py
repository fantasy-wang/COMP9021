'''
You might find the zip() function useful, though you can also do without it.
'''

from random import randrange, seed
import math


def display(square, size):
    print('\n'.join(' '.join(f'{x:{size}}' for x in row) for row in square))

def f(for_seed, n, upper_bound):
    '''
    >>> f(0, 2, 2)
    Here is the square: 
    1 1
    0 1
    It is not a good square because it contains duplicates, namely: 1
    >>> f(0, 3, 5)
    Here is the square: 
    3 3 0
    2 4 3
    3 2 3
    It is not a good square because it contains duplicates, namely: 2 3
    >>> f(0, 6, 50)
    Here is the square: 
    24 48 26  2 16 32
    31 25 19 30 22 37
    13 32  8 18  8 48
     6 39 16 34 45 38
     9 19  6 46  4 43
    21 30 35  6 22 27
    It is not a good square because it contains duplicates, namely: 6 8 16 19 22 30 32 48
    >>> f(0, 2, 50)
    Here is the square: 
    24 48
    26  2
    It is a good square.
    Ordering the elements from left to right column, from top to bottom, yields:
     2 26
    24 48
    >>> f(0, 3, 100)
    Here is the square: 
     49  97  53
      5  33  65
     62  51  38
    It is a good square.
    Ordering the elements from left to right column, from top to bottom, yields:
      5  49  62
     33  51  65
     38  53  97
    >>> f(0, 6, 5000)
    Here is the square: 
    3155 3445  331 2121 4188 3980
    3317 2484 3904 2933 4779 1789
    4134 1140 2308 1144  776 2052
    4362 4930 1203 2540  809  604
    2704 3867 4585  824 2898 3556
    2590 1675 4526 3907 3626 4270
    It is a good square.
    Ordering the elements from left to right column, from top to bottom, yields:
     331 1144 2308 2933 3867 4270
     604 1203 2484 3155 3904 4362
     776 1675 2540 3317 3907 4526
     809 1789 2590 3445 3980 4585
     824 2052 2704 3556 4134 4779
    1140 2121 2898 3626 4188 4930
    
    '''
    seed(for_seed)
    square = [[randrange(upper_bound) for _ in range (n)] for _ in range(n)]
    duplicates = set()
    ordered_square = [[]]
    print('Here is the square: ')
    display(square, len(str(upper_bound)))
    if square==[]:
        duplicates = []
    else:
        list1 = square
        list2 = []
        list3 = []
        for i in range(len(list1)):
            for j in range(len(list1[i])):
                list2.append(list1[i][j])
        for i in range(len(list2)):
            for j in range(i+1, len(list2)):
                if j<len(list2):
                    if list2[i]==list2[j]:
                        list3.append(str(list2[i]))
        if len(list3) >= 1:
            list3 = list(set(list3))
            for i in range(len(list3)):
                list3[i]=int(list3[i])
            list3.sort()
            duplicates = list3
        else:
            a1 = math.sqrt(len(list2))
            for i in range(len(list2)):
                list2[i] = int(list2[i])
            list2.sort()
            for i in range(len(list2)):
                list2[i]=str(list2[i])
            for i in range(len(list2)):

            print(list2)
            # ordered_square = list2
    # Insert your code here
    if duplicates:
        print('It is not a good square because it contains duplicates, namely: ', end = '')
        print(' '.join(str(e) for e in sorted(duplicates)))
    else:
        print('It is a good square.')
        print('Ordering the elements from left to right column, from top to bottom, yields:')
        display(ordered_square, len(str(upper_bound)))

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
