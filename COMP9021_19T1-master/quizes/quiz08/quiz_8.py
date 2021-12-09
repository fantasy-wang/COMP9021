# A polynomial object can be created from a string that represents a polynomial
# as sums or differences of monomials.
# - Monomials are ordered from highest to lowest powers.
# - All factors are strictly positive, except possibly for the leading factor
# - For nonzero powers, factors of 1 are only implicit.
# A single space surrounds + and - signs between monomials.

# Written by *** and Eric Martin for COMP9021


import re  # split() suffices though
from collections import defaultdict
from copy import deepcopy


class Polynomial:

    def __init__(self, polynomial=None):
        pass
        # REPLACE pass ABOVE WITH YOUR CODE
        # re.findall('([+|-]\s*\w+)', a)

        # set default int
        result = defaultdict(int)

        factors = {"-": -1, "+": 1}

        # x^3 - x + 4

        # not None
        if polynomial:
            split_list = polynomial.split(" ")
            # True 表示整数，False  表示复数
            factor = 1
            for item in split_list:
                if item in factors:
                    factor = factors.get(item)
                    continue

                power = 0
                item = item.replace("^", "")
                numbers = item.split("x")
                # 当item 是 -5，x,5x, 5x5
                if numbers[0]:
                    if numbers[0] == '-':
                        factor = -1
                    else:
                        factor = factor * int(numbers[0])
                if len(numbers) == 2:
                    if not numbers[1]:
                        numbers[1] = '1'
                    power = int(numbers[1])
                # 保存得到的结果
                result[power] = factor

        self.polynomial = result

        print(self.polynomial)

        self.max_degree = 0
        if result:
            self.max_degree = max(result.keys())

    # DEFINE OTHER METHODS
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.poly1d.html#numpy.poly1d
    def __add__(self, other):
        max_degree = max(self.max_degree, other.max_degree)
        result = defaultdict(int)
        for degree in range(max_degree + 1):
            value = self.polynomial.get(degree, 0) + other.polynomial.get(degree, 0)
            if value != 0:
                result[degree] = value

        new_polynomial = Polynomial()
        new_polynomial.polynomial = result
        if result:
            new_polynomial.max_degree = max(*result.keys(), 0)
        return new_polynomial


    def __mul__(self, other):
        result = defaultdict(int)

        for degree1, coefficient1 in self.polynomial.items():
            for degree2, coefficient2 in other.polynomial.items():
                new_degree = degree1 + degree2
                new_coefficient = coefficient1 * coefficient2 + result.get(new_degree, 0)
                # 如果系数大于0 放入结果集
                if new_coefficient != 0:
                    result[new_degree] = new_coefficient

        new_polynomial = Polynomial()
        new_polynomial.polynomial = result
        if result:
            new_polynomial.max_degree = max(*result.keys(), 0)
        return new_polynomial

    def __str__(self):
        if self.polynomial:
            keys = reversed(sorted(self.polynomial.keys()))
            result = ""

            for key in keys:
                value = self.polynomial.get(key)
                items = []
                if key > 1:
                    items.append(str(key))
                    items.append("^")
                    items.append("x")
                elif key == 1:
                    items.append("x")

                # value 不可能为0
                if value == 1 and items:
                    items.append(" + ")
                elif value == -1 and items:
                    items.append(" - ")
                elif value > 0:
                    items.append(str(abs(value)))
                    items.append(" + ")
                elif value < 0:
                    items.append(str(abs(value)))
                    items.append(" - ")
                expression = "".join(reversed(items))

                if result:
                    result += expression
                else:
                    result = expression.replace("+", "").replace(" ", "").strip()

            return result

        else:
            return "0"


def test():
    """
    >>> p = Polynomial()
    >>> print(p + Polynomial('2'))
    2
    >>> print(p)
    0
    >>> p += Polynomial('2')
    >>> print(p)
    2
    >>> p = Polynomial('3')
    >>> print(p + Polynomial('-3'))
    0
    >>> print(p)
    3
    >>> p += Polynomial('-3')
    >>> print(p)
    0
    >>> p = Polynomial('x')
    >>> print(p + Polynomial('2x^3 + x - 4'))
    2x^3 + 2x - 4
    >>> print(p)
    x
    >>> p += Polynomial('2x^3 + x - 4')
    >>> print(p)
    2x^3 + 2x - 4
    >>> p = Polynomial('4x^5 - x^2 + 6')
    >>> print(p * Polynomial('x^3 - x + 4'))
    4x^8 - 4x^6 + 15x^5 + 7x^3 - 4x^2 - 6x + 24
    >>> print(p)
    4x^5 - x^2 + 6
    >>> p *= Polynomial('x^3 - x + 4')
    >>> print(p)
    4x^8 - 4x^6 + 15x^5 + 7x^3 - 4x^2 - 6x + 24
    >>> p = Polynomial('x^4 - x^3 + x^2 - x')
    >>> print(p * Polynomial('-2x^3 + 3x^2 - 4x + 5'))
    -2x^7 + 5x^6 - 9x^5 + 14x^4 - 12x^3 + 9x^2 - 5x
    >>> p *= Polynomial('-2x^3 + 3x^2 - 4x + 5')
    >>> print(p)
    -2x^7 + 5x^6 - 9x^5 + 14x^4 - 12x^3 + 9x^2 - 5x
    >>> p = Polynomial('x')
    >>> print(p + Polynomial('-x'))
    0
    >>> p = Polynomial('2x')
    >>> print(p + Polynomial('-x'))
    x
    >>> p = Polynomial('x')
    >>> print(p + Polynomial('-2x'))
    -x
    """


if __name__ == '__main__':
    # import doctest

    # doctest.testmod()

    p1 = Polynomial('2x^2 - 1')
    print(p1)

    #p = Polynomial('x')
    # print(p + Polynomial('-x'))
