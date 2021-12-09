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


from collections import namedtuple, deque
import numpy as np
from random import seed, randrange
import sys

Point = namedtuple('Point', 'x y')


def display_grid():
    for row in grid:
        print('   ', ' '.join(str(int(e)) for e in row))


def valid(pt):
    return 0 <= pt.x < width and 0 <= pt.y < height


def nb_of_good_paths(pt_1, pt_2):
    # REPLACE pass ABOVE WITH YOUR CODE
    number_of_solutions = 0

    # left right, up and down
    # format: x,y
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    # two points are not the same
    if pt_1 != pt_2:
        # create new deque
        search_queue = deque()
        # add the initial point
        search_queue.append([(pt_1.x, pt_1.y)])

        # search all the probability
        while search_queue:
            # get the current search path
            current_path = search_queue.popleft()
            # get the current search point
            (current_point_x, current_point_y) = current_path[-1]
            # check the current point
            # 1.check four directions
            for direction in directions:
                # get the variations
                off_size_x, off_size_y = direction
                new_point_x = current_point_x + off_size_x
                new_point_y = current_point_y + off_size_y

                # 2.check the new point surely in the grid
                if 0 <= new_point_x < width and 0 <= new_point_y < height:
                    # 3.check the new point value must be 1 and haven't be searched
                    if grid[new_point_y][new_point_x] and (new_point_x, new_point_y) not in current_path:
                        # 4 check one direction less two steps
                        # get the last three point
                        last_three_points = current_path[-3:]
                        axes = list(zip(*last_three_points))
                        # check x axis and y axis
                        if (new_point_x,) * 3 == axes[0] or (new_point_y,) * 3 == axes[1]:
                            # select the other direction
                            continue
                        else:
                            # if the new point is the target point
                            if new_point_x == pt_2.x and new_point_y == pt_2.y:
                                number_of_solutions += 1
                                continue
                            # add searched path
                            search_queue.append(current_path + [(new_point_x, new_point_y)])

    # return the number of solutions
    return number_of_solutions


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
