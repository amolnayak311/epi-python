import functools
from sys import exit

from test_framework import generic_test, test_utils
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)



def _dutch_flag_partition_1(pivot_index, A):    
    if len(A) < 2:    
        return
    
    A[0], A[pivot_index] = A[pivot_index], A[0]
    left, right = 1, len(A) - 1
    
    #Pass1, Get everything less than or equal to pivot on the left
    pivot_elem = A[0] 
    while left <= right:
        if A[left] > pivot_elem:
            A[left], A[right] = A[right], A[left]
            right -=1 
        else:
            left += 1
    
    #Pass2, Get everything equal to pivot on the right
    left = 1
    while left <= right:
        if A[left] == pivot_elem:
            A[left], A[right] = A[right], A[left]
            right -=1 
        else:
            left += 1
    #Final Swap of the pivot to its rightful position       
    A[0], A[right] = A[right], A[0]     


#One pass implementation
def _dutch_flag_partition_2(pivot_index, A):
    if len(A) == 1:
        return
    
    less, equal, more = 0, 0, len(A) - 1
    pivot = A[pivot_index]
    while equal <= more:
        if A[equal] < pivot:
            A[less], A[equal] = A[equal], A[less] 
            equal += 1
            less += 1
        elif A[equal] == pivot:
            equal += 1
        else:
            A[equal], A[more] = A[more], A[equal]
            more -= 1     



def dutch_flag_partition(pivot_index, A):
    #_dutch_flag_partition_1(pivot_index, A)
    _dutch_flag_partition_2(pivot_index, A)


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
