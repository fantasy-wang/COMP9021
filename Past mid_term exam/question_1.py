from random import seed, randint
import sys


def f(arg_for_seed, nb_of_elements, max_element):
    '''
    >>> f(0, 0, 10)
    Here is L: []
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        []
    >>> f(0, 1, 10)
    Here is L: [6]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6]]
    >>> f(0, 2, 10)
    Here is L: [6, 6]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6]]
    >>> f(0, 3, 10)
    Here is L: [6, 6, 0]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6], [0]]
    >>> f(0, 4, 10)
    Here is L: [6, 6, 0, 4]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6], [0, 4]]
    >>> f(0, 5, 10)
    Here is L: [6, 6, 0, 4, 8]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6], [0, 4, 8]]
    >>> f(0, 6, 10)
    Here is L: [6, 6, 0, 4, 8, 7]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6], [0, 4, 8], [7]]
    >>> f(0, 7, 10)
    Here is L: [6, 6, 0, 4, 8, 7, 6]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6], [0, 4, 8], [7], [6]]
    >>> f(3, 10, 6)
    Here is L: [1, 4, 4, 1, 2, 4, 3, 5, 4, 0]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[1, 4], [1, 2, 4], [3, 5], [4], [0]]
    >>> f(3, 15, 8)
    Here is L: [3, 8, 2, 5, 7, 1, 0, 7, 4, 8, 3, 3, 7, 8, 8]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[3, 8], [2, 5, 7], [1], [0, 7], [4, 8], [3, 7, 8]]
    '''
    if nb_of_elements < 0:
        sys.exit()
    seed(arg_for_seed)
    L = [randint(0, max_element) for _ in range(nb_of_elements)]
    print('Here is L:', L)
    R = []
    list1=[]
    list2 = []
    if len(L)>1:
        list2.append(L[0])
        for i in range(len(L)):
            if i + 1 < len(L):
                if L[i] != L[i + 1]:
                    list2.append(L[i + 1])
    if len(L)==0:
        R = []
    elif len(L)==1:
        R=[L]
    elif len(list2)==1:
        R=[list2]
    elif len(list2)>1:
        list1 = [list2[0]]
        for i in range(len(list2)):
            if i+1 < len(list2):
                if list2[i]<list2[i+1]:
                    list1.append(list2[i+1])
                    if i+1 == len(list2)-1:
                        R.append(list1)
                        break
                else:
                    R.append(list1)
                    if i+1 == len(list2)-1:
                        R.append([list2[i+1]])
                        break
                    else:
                        list1 = [list2[i+1]]
                        continue






    # Insert your code here
    print('The decomposition of L into increasing sequences,')
    print('    with consecutive duplicates removed, is:\n   ', R)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
