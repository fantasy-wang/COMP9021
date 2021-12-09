# Written by Eric Martin for COMP9021


import sys
from random import seed, randint, randrange

from itertools import zip_longest

try:
    arg_for_seed, upper_bound, length = \
        (int(x) for x in input('Enter three integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


def length_of_longest_increasing_sequence(L):
    pass
    # REPLACE pass ABOVE WITH  YOUR CODE

    # result value
    length_of_longest = int(len(L) > 0)
    # if > 0
    if length_of_longest:
        length_temp, first = length_of_longest, L[0]
        # for each
        for i in range(1, len(L) * 2 - 1):
            # if it is the largest length
            if length_of_longest == len(L):
                break

            if first <= L[i % len(L)]:
                # plus + 1
                length_temp += 1
            else:
                # set default
                length_temp = 1
            # set new value
            first = L[i % len(L)]
            # get max value
            length_of_longest = max(length_of_longest, length_temp)
    # result
    return length_of_longest


def max_int_jumping_in(L):
    pass
    # REPLACE pass ABOVE WITH  YOUR CODE
    # 方法1
    # indexs = list(range(len(L)))
    # zip_list = zip_longest(indexs,L)
    indexs = {}
    for index, value in enumerate(L):
        indexs[index] = value
    max_length = 0
    result = ""
    for num in L:
        # clear list
        jumping_list = [num]
        # set default value
        while num < len(L) and num in indexs:
            num = indexs[num]
            jumping_list.append(num)
            if num in jumping_list:
                break

        if len(jumping_list) > max_length:
            max_length = len(jumping_list)
            result = "".join((str(e) for e in jumping_list))

    return result


seed(arg_for_seed)
L_1 = [randint(0, upper_bound) for _ in range(length)]
print('L_1 is:', L_1)
print('The length of the longest increasing sequence\n'
      '  of members of L_1, possibly wrapping around, is:',
      length_of_longest_increasing_sequence(L_1), end='.\n\n'
      )
L_2 = [randrange(length) for _ in range(length)]
print('L_2 is:', L_2)
print('The maximum integer built from L_2 by jumping\n'
      '  as directed by its members, from some starting member\n'
      '  and not using any member more than once, is:',
      max_int_jumping_in(L_2)
      )
