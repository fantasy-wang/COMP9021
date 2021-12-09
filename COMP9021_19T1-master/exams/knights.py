# Randomly fills an array of size 10x10 True and False, displayed as 1 and 0,
# and outputs the number chess knights needed to jump from 1s to 1s
# and visit all 1s (they can jump back to locations previously visited).
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys
from itertools import chain, product, combinations, combinations_with_replacement, permutations

dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end='')
        print(' '.join(grid[i][j] and '1' or '0' for j in range(dim)))
    print()


def explore_board():
    pass
    # Replace pass above with your code
    row_length = len(grid)
    column_length = len(grid[0])
    count = 0
    for row_index in range(row_length):
        for column_index in range(column_length):
            if grid[row_index][column_index] == 1:
                count_number((row_index, column_index))
                count += 1

    return count


def count_number(point):
    row_length = len(grid)
    column_length = len(grid[0])
    (row_index, column_index) = point
    grid[row_index][column_index] = 0

    x = (1, -1)
    y = (2, -2)
    # [(1,2) (1,-2) (-1,2) (-1,-2)]
    directions = product(x, y)
    x = (2, -2)
    y = (1, -1)

    # (2,1) (2,-1) (-2,1) (-2,-1)
    directions = chain(directions, product(x, y))
    directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    for direction in directions:
        new_column_index = column_index + direction[0]
        new_row_index = row_index + direction[1]
        if 0 <= new_column_index < column_length \
                and 0 <= new_row_index < row_length \
                and grid[new_row_index][new_column_index] == 1:
            count_number((new_row_index, new_column_index))


try:
    for_seed, n = (int(i) for i in input('Enter two integers: ').split())
    if not n:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
if n > 0:
    grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
else:
    grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
nb_of_knights = explore_board()
if not nb_of_knights:
    print('No chess knight has explored this board.')
elif nb_of_knights == 1:
    print(f'At least 1 chess knight has explored this board.')
else:
    print(f'At least {nb_of_knights} chess knights have explored this board')
