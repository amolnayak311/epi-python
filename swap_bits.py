def swap_bits(x, i, j):
    
    if (x >> i) & 1 != (x >> j) & 1:
        #Only if ith and jth bit are different
        #xoring the values will toggle their state this swapping the bits
        
        mask = (1 << i) | (1 << j)
        x ^= mask
    return x


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(generic_test.generic_test_main('swap_bits.tsv', swap_bits))
