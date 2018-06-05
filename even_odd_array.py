import collections
import functools
from sys import exit

from test_framework import generic_test, test_utils
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(A):
    left_ptr, right_ptr = 0, len(A)  - 1
    while left_ptr < right_ptr:
        if A[left_ptr] & 1:
            A[left_ptr], A[right_ptr] = A[right_ptr], A[left_ptr]
            right_ptr -= 1 
        else:
            left_ptr += 1
    


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure("Even elements appear in odd part")
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure("Elements mismatch")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.tsv', even_odd_wrapper))
