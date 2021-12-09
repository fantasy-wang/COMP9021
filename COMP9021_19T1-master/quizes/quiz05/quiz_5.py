# Prompts the user for a positive integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived positive integer that codes the set of running sums
# ot the members of S when those are listed in increasing order.
#
# Written by  Chang Su and Eric Martin for COMP9021


from itertools import accumulate
import sys

try:
    encoded_set = int(input('Input a positive integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


# POSSIBLY DEFINE OTHER FUNCTIONS
def display(L):
    print('{',end = '')
    print(', '.join(str(i) for i in L),end = '')
    print('}')

def display_encoded_set(encoded_set):
    result_list = []
    binary = bin(encoded_set)[2:]
    binary_list = binary[::-1]
    for i in range(len(binary_list)-1,-1,-1):
        if i % 2 == 0:
            if binary_list[i] == '1':
                result_list.append(int(i/2))
        if i % 2 != 0:
            if binary_list[i] == '1':
                result_list.append(int(-(i//2)-1))
    result_list.sort()
    display(result_list)
   # REPLACE pass ABOVE WITH CODE TO PRINT OUT ENCODED SET (WITH print() STATEMENTS)


def code_derived_set(encoded_set):
    encoded_running_sum = 0
    sum = 0
    sum_list = []
    result_list = []
    binary = bin(encoded_set)[2:]
    binary_list = binary[::-1]
    for i in range(len(binary_list) - 1, -1, -1):
        if i % 2 == 0:
            if binary_list[i] == '1':
                result_list.append(int(i / 2))
        if i % 2 != 0:
            if binary_list[i] == '1':
                result_list.append(int(-(i // 2) - 1))
    result_list.sort()
    for i in result_list:
        sum += i
        sum_list.append(sum)
    sum_list = list(set(sum_list))
    sum_list.sort()
    #display(sum_list)
    for i in sum_list:
        if i < 0:
            encoded_running_sum = encoded_running_sum + 2 ** (-(i * 2) - 1)
        else:
            encoded_running_sum = encoded_running_sum + 2 ** (i * 2)
    #print(f'{encoded_running_sum:6}')

    #print('sum_list', sum_list)

    # REPLACE THIS COMMENT WITH YOUR CODE
    return encoded_running_sum


print('The encoded set is: ', end='')
display_encoded_set(encoded_set)
encoded_running_sum = code_derived_set(encoded_set)
print('The derived encoded set is: ', end='')
display_encoded_set(encoded_running_sum)
print('  It is encoded by:', encoded_running_sum)


