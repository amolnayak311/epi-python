
def closest_int_same_bit_count(x):
    first_non_set = ~x & (x + 1)
    first_set = x & ~(x - 1)
    if first_set > first_non_set:
        #Unset first set bit and set the adjacent bit on the right which is not set
        x ^= first_set
        x |= first_set >> 1        
    else:
        #Set first non set bit and adjacent bit on the right which is set to 0
        x |= first_non_set
        x ^= first_non_set >> 1
    return x

from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("closest_int_same_weight.tsv",
                                       closest_int_same_bit_count))

    #closest_int_same_bit_count(39698800462691)