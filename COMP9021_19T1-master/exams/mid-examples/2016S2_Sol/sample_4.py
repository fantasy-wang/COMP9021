
def is_heterosquare(square):
    '''
    A heterosquare of order n is an arrangement of the integers 1 to n**2 in a square,
    such that the rows, columns, and diagonals all sum to DIFFERENT values.
    In contrast, magic squares have all these sums equal.
    
    
    >>> is_heterosquare([[1, 2, 3],\
                         [8, 9, 4],\
                         [7, 6, 5]])
    True
    >>> is_heterosquare([[1, 2, 3],\
                         [9, 8, 4],\
                         [7, 6, 5]])
    False
    >>> is_heterosquare([[2, 1, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    True
    >>> is_heterosquare([[1, 2, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    False
    '''
    n = len(square)
    if any(len(line) != n for line in square):
        return False
    # Insert your code here
    if n % 2 == 0:
        list_of_sum = []
        sum_of_column = 0
        sum_of_dia_1 = 0
        sum_of_dia_2 = 0
        for i in range(n):
            sum_of_row = sum(square[i])
            list_of_sum.append(sum_of_row)
            sum_of_row = 0
            for j in range(n):
                if j == i:
                    sum_of_dia_1 += square[i][j]
                elif i + j == n - 1:
                    sum_of_dia_2 += square[i][j]
        list_of_sum.append(sum_of_dia_1)       
        list_of_sum.append(sum_of_dia_2)
        for i in range(n):
            for j in range(n):
                sum_of_column += square[j][i]
            list_of_sum.append(sum_of_column)
            sum_of_column = 0
        #print(list_of_sum)

        if len(list_of_sum) == len(set(list_of_sum)):
            return True
        else:
            return False

       
    if n % 2 != 0:
        list_of_sum = []
        sum_of_column = 0
        sum_of_dia_1 = 0
        sum_of_dia_2 = 0
        middle_point = square[n//2][n//2]
        for i in range(n):
            sum_of_row = sum(square[i])
            list_of_sum.append(sum_of_row)
            sum_of_row = 0
            for j in range(n):
                if j == i and i != n // 2:
                    sum_of_dia_1 += square[i][j]
                elif i + j == n - 1 and i != n // 2:
                    sum_of_dia_2 += square[i][j]
        sum_of_dia_1 += middle_point
        sum_of_dia_2 += middle_point
        list_of_sum.append(sum_of_dia_1)       
        list_of_sum.append(sum_of_dia_2)
        for i in range(n):
            for j in range(n):
                sum_of_column += square[j][i]
            list_of_sum.append(sum_of_column)
            sum_of_column = 0
        #print(list_of_sum)

        if len(list_of_sum) == len(set(list_of_sum)):
            return True
        else:
            return False

# Possibly define other functions

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
