# Randomly fills a grid with True and False, with width, height and density
# controlled by user input, and computes the number of all "good paths" that link
# a point of coordinates (x1, y1) to a point of coordinates (x2, y2)
# (x1 and x2 are horizontal coordinates, increasing from left to right,
# y1 and y2 are vertical coordinates, increasing from top to bottom,
# both starting from 0), that is:
# - paths that go through nothing but True values in the grid
# - paths that never go through a given point in the grid more than once;
# - paths that never keep the same direction (North, South, East, West) over
#   a distance greater than 2.
#
# Written by *** and Eric Martin for COMP9021


from collections import namedtuple
import numpy as np
from random import seed, randrange
import sys


Point = namedtuple('Point', 'x y')


def display_grid():
    for row in grid:
        print('   ', ' '.join(str(int(e)) for e in row))

def valid(pt):
    return 0 <= pt.x < width and 0 <= pt.y < height

def nb_of_good_paths(pt_1, pt_2, list1 = [], list2 = [], list3 = []):
    if grid[pt_2.x][pt_2.y] == 0:
        return 0
    if pt_1.x == pt_2.x and pt_1.y == pt_2.y:
        return len(list3)
    if pt_1.x == pt_2.x - 1 and pt_1.y == pt_2.y and grid[pt_1.y][
        pt_1.x] == 1 or pt_1.x == pt_2.x + 1 and pt_1.y == pt_2.y and grid[pt_1.y][
        pt_1.x] == 1 or pt_1.x == pt_2.x and pt_1.y == pt_2.y - 1 and grid[pt_1.y][
        pt_1.x] == 1 or pt_1.x == pt_2.x and pt_1.y == pt_2.y + 1 and grid[pt_1.y][pt_1.x] == 1:
        list3.append(list2)
    if grid[pt_1.y][pt_1.x] == 1:
        list1 = [pt_1.x, pt_1.y]
        list2.append(list1)
        for i in range(len(list2)):
            for j in range(i+1, len(list2)):
                if j < len(list2):
                    if list2[i] == list2[j]:
                        list2.remove(list2[j])
        if grid[pt_1.y + 1][pt_1.x] and len(list2) > 2:
            if grid[pt_1.y + 1][pt_1.x] == 1 and pt_1.x == list2[-3][0] and pt_1.y + 1 - list2[-3][1] > 2 or \
                    grid[pt_1.y + 1][pt_1.x] == 1 and pt_1.x - list2[-3][0] > 2 and pt_1.y + 1 == list2[-3][1]:
                pt_1 = Point(pt_1.y+1, pt_1.x)
                nb_of_good_paths(pt_1, pt_2, list1, list2, list3)
    else:
        return 0

    # REPLACE pass ABOVE WITH YOUR CODE

# POSSIBLY DEFINE OTHER FUNCTIONS
try:
    for_seed, density, height, width = (abs(int(i)) for i in
                                                  input('Enter four integers: ').split()
                                       )
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
if not density:
    density = 1
seed(for_seed)
grid = np.array([randrange(density) > 0
                              for _ in range(height * width)
                ]
               ).reshape((height, width))
print('Here is the grid that has been generated:')
display_grid()
try:
    i1, j1, i2, j2 = (int(i) for i in input('Enter four integers: ').split())
    pt_1 = Point(i1, j1)
    pt_2 = Point(i2, j2)
    if not valid(pt_1) or not valid(pt_2):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
print('Will compute the number of good paths '
      f'from ({pt_1.x}, {pt_1.y}) to ({pt_2.x}, {pt_2.y})...'
     )
paths_nb = nb_of_good_paths(pt_1, pt_2)
if not paths_nb:
    print('There is no good path.')
elif paths_nb == 1:
    print('There is a unique good path.')
else:
    print('There are', paths_nb, 'good paths.')