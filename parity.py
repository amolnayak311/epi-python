#Simple Brute force approach
#Toggle the bits based on the least significant bit position
def parity_bruteforce(x):
    par = 0
    while x:
        par ^= x & 1
        x >>= 1

    return par

#
# x & (x - 1) toggles only the last set bit. When all bits are set, x becomes 0
# par ^= 1 toggles the count 
#
def parity_improved(x):
    par = 0
    while x:
        x &= (x - 1)
        par ^= 1

    return par

#Constant time preparing map
lookup = {i: parity_improved(i) for i in range(65537)}
#
# Approach creates a dict of all possible 16 bit numbers and then finds the 
# parity of these 16 bit portions of the numbers. The parity of these 4 portions form the
# parity of entire number.     
#
def parity_lookup(x):
    mask = 0xFFFF
    return lookup[x & mask] ^ lookup[(x >> 16) & mask] ^ lookup[(x >> 32) & mask] ^ lookup[(x >> 48) & mask]


#
# Since xor is associative as well as commutative. We can find parity of  a 64 bit number by doing xor of two 32 bit numbers
# We can repeat this till we reach a single bit. Thus we perform no more than log(64) operations  
# The last bit tells us if the total number of bits are even or odd. Notice how the least 
 # significant bits gain more and more importance 
#
def parity_associative(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    
    return x & 1

    

def parity(x):
    # Implement this placeholder.
    #return parity_bruteforce(x)
    #return parity_improved(x)
    #return parity_lookup(x)
    return parity_associative(x)

from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.tsv', parity))
