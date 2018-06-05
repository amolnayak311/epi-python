def plus_one(A):
    # Implement this placeholder
    carry = 1
    for i in reversed(range(len(A))):
        res = A[i] + carry
        carry, A[i] = (0, res) if res < 10 else (1, 0)  
        if carry == 0:
            break
        
    return A if carry == 0 else [1] + A


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.tsv", plus_one))
