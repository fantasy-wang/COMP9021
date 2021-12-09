from math import sqrt
def is_prime(n):
    # Only used to test odd numbers.
    print(list((n % d for d in range(3, round(sqrt(n)) + 1, 2))))
    return all(n % d for d in range(3, round(sqrt(n)) + 1, 2))


print(is_prime(28))