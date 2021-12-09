# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and determines the size of the largest
# isosceles triangle, consisting of nothing but 1s and whose base can be either
# vertical or horizontal, pointing either left or right or up or down.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
import numpy as np

def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))


def size_of_largest_isosceles_triangle():
    pass
    # REPLACE pass WITH YOUR CODE
    max_size = 0
    grid_ext = np.array(grid)
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            max_size = max(max_size,get_size_of_grid(grid_ext,(x,y)))
            grid_ext = np.rot90(grid_ext)
            max_size = max(max_size, get_size_of_grid(grid_ext, (x, y)))
            grid_ext = np.rot90(grid_ext)
            max_size = max(max_size, get_size_of_grid(grid_ext, (x, y)))
            grid_ext = np.rot90(grid_ext)
            max_size = max(max_size, get_size_of_grid(grid_ext, (x, y)))
            grid_ext = np.rot90(grid_ext)
    return max_size

# POSSIBLY DEFINE OTHER FUNCTIONS
def get_size_of_grid(grid_ext, point):
    x, y = point
    max_size = 0
    # 如果当前的位置是0，直接跳过
    if (grid_ext[y, x] != 0):
        # 求到边缘还剩下多少长度
        left_x_length = len(grid_ext[0])
        for i in range(3, left_x_length, 2):
            size = (i + 1) // 2
            if (x + i) < len(grid_ext[0]) and (y + size) < len(grid_ext):
                current_grid = grid_ext[y:y + size, x: x + i]
                A = np.triu(current_grid,0)
                B = np.fliplr(A)
                C = np.triu(B,0)
                if np.count_nonzero(C) == size * size:
                    max_size = max(max_size,size)
    return max_size




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
