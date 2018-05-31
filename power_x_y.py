def power_iter(x, y):    
    res = 1.0
    x, power = (x, y) if y > 0 else (1 / x, -y)
    
    while power:
        if power & 1:
            res *= x
        
        x *= x    
        power >>= 1
    
    return  res   

#Recursive and more succinct implementation
def power_rec_(x, y):  
    if y == 0:
        return 1
    if y == 1:
        return x
    
    h = power_rec_(x, y // 2)
    return x * h * h if y & 1 else h * h
  
def power_rec(x, y):
    return power_rec_(x, y) if y >= 0 else  power_rec_(1 / x, -y)


def power(x, y):    
    #return power_iter(x, y)
    return power_rec(x, y)


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.tsv', power))
    