# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and determines the size of the largest
# isosceles triangle, consisting of nothing but 1s and whose base can be either
# vertical or horizontal, pointing either left or right or up or down.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))


def size_of_largest_isosceles_triangle():
    a1 = 0
    a2 = 0
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    for i in range(10):
        for j in range(10):
            if grid[i][j] != 0:
                a2 = 1
                a1 = 0
                for k in range(i+1, 10):
                    for n in range(j-(k-i), j+k-i+1):
                        if n < 0 or n > 9:
                            a1 += 0
                        else:
                            if grid[k][n] != 0:
                                a1 += 1
                    if a1 == 2*(k-i)+1:
                        a2 += 1
                        a1 = 0
                    else:
                        a1 = -1
                list1.append(a2)
    #
    for i in range(9, -1, -1):
        for j in range(10):
            list2.append(grid[j][i])
        list3.append(list2)
        list2 = []
    for i in range(10):
        for j in range(10):
            if list3[i][j] != 0:
                a2 = 1
                a1 = 0
                for k in range(i+1, 10):
                    for n in range(j-(k-i), j+k-i+1):
                        if n < 0 or n > 9:
                            a1 += 0
                        else:
                            if list3[k][n] != 0:
                                a1 += 1
                    if a1 == 2*(k-i)+1:
                        a2 += 1
                        a1 = 0
                    else:
                        a1 = -1
                list1.append(a2)
    #
    for i in range(9, -1, -1):
        for j in range(10):
            list2.append(list3[j][i])
        list4.append(list2)
        list2 = []
    for i in range(10):
        for j in range(10):
            if list4[i][j] != 0:
                a2 = 1
                a1 = 0
                for k in range(i + 1, 10):
                    for n in range(j - (k - i), j + k - i + 1):
                        if n < 0 or n > 9:
                            a1 += 0
                        else:
                            if list4[k][n] != 0:
                                a1 += 1
                    if a1 == 2 * (k - i) + 1:
                        a2 += 1
                        a1 = 0
                    else:
                        a1 = -1
                list1.append(a2)
    #
    for i in range(9, -1, -1):
        for j in range(10):
            list2.append(list4[j][i])
        list5.append(list2)
        list2 = []
    for i in range(10):
        for j in range(10):
            if list5[i][j] != 0:
                a2 = 1
                a1 = 0
                for k in range(i+1, 10):
                    for n in range(j-(k-i), j+k-i+1):
                        if n < 0 or n > 9:
                            a1 += 0
                        else:
                            if list5[k][n] != 0:
                                a1 += 1
                    if a1 == 2*(k-i)+1:
                        a2 += 1
                        a1 = 0
                    else:
                        a1 = -1
                list1.append(a2)
    if list1:
        return max(list1)
    else:
        return 0
# REPLACE pass WITH YOUR CODE

# POSSIBLY DEFINE OTHER FUNCTIONS


try:
    arg_for_seed, density = (abs(int(x)) for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
print('The largest isosceles triangle has a size of',
      size_of_largest_isosceles_triangle()
      )