def reverse(x):
    res = 0
    x, isNeg = (-x, True) if x < 0 else (x, False) 
    while x > 0:
        rem = x % 10
        x //= 10
        res = 10 * res + rem
    
    return -res if isNeg else res


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(generic_test.generic_test_main('reverse_digits.tsv', reverse))
    
