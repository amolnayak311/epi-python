from reverse_digits import reverse

#From test cases Negative number are not considered palindrome. The code works just fine for negative numbers too
# Just explicitly making them false for negative numbers
def is_palindrome_number(x):    
    return False if x < 0 else x == reverse(x)


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.tsv",
                                       is_palindrome_number))
    