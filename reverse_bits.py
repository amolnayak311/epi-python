

# Doing format(<number>, #018b) gives us number formatted as binary with results width as 18 chars. The first two being 0b
# format(<number>, '#018b')[2:][::-1] gets the binary  representation of a number as string and reverses it

#Precomputed reverse of numbers
precomputed = {i : int(format(i, '#018b')[2:][::-1], 2) for i in range(65536)}   

def reverse_bits(x):
    # Implement this placeholder.
    mask = 0xFFFF
    x, isNeg =  (-x, True) if x < 0 else (x, False)    
    res =  0 | \
            precomputed[x & mask] << 48 | \
            precomputed[(x >> 16) & mask] << 32 | \
            precomputed[(x >> 32) & mask] << 16 | \
            precomputed[(x >> 48) & mask]
    return -res if isNeg else res  


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(generic_test.generic_test_main("reverse_bits.tsv", reverse_bits))
