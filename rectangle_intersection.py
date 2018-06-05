import collections
from sys import exit

from test_framework import generic_test, test_utils
from test_framework.test_failure import PropertyName

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


#Assuming the top left corner if the rectangle is x, y and y increases as we go down
#and x increases as we go right
def does_intersect(R1, R2):
    return R1.x <= (R2.x + R2.width) and R2.x <= (R1.x + R1.width) and \
        R1.y <= (R2.y + R2.height) and R2.y <= (R1.y + R1.height) 
    

def intersect_rectangle(R1, R2):
    # Implement this placeholder.
    if does_intersect(R1, R2):
        x = max(R1.x, R2.x)
        y = max(R1.y, R2.y)
        width = min(R1.x + R1.width, R2.x + R2.width) - x
        height = min(R1.y + R1.height, R2.y + R2.height) - y
        return Rectangle(x, y, width, height)
        
    else:
        #Inferring from failed test cases that this is the expected result if no intersection
        return Rectangle(0, 0, -1, -1)


def intersect_rectangle_wrapper(R1, R2):
    return intersect_rectangle(Rectangle(*R1), Rectangle(*R2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'rectangle_intersection.tsv',
            intersect_rectangle_wrapper,
            res_printer=res_printer))
