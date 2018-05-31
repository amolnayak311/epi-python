def add(a1, a2):
    #
    # Element by element addition of  two arrays a1 and a2
    # Addition starts from Least Significant Digit
    
    l1 = len(a1)
    l2 = len(a2)
    
    if l1 == 0:
        return a2
    elif l2 == 0:
        return a1
    
    l = min(l1, l2)
    carry = 0
    partial_res = [0] * l
    for i in range(-1, -1-l, -1):
        res = a1[i] + a2[i] + carry
        (carry, partial_res[i]) = (1, res - 10) if res >= 10 else (0, res)
    
    if l1 == l2:
        return partial_res if carry == 0 else [1] + partial_res
    
    left = [a1[i]  for i in range(0, l1 - l2)] if l1 > l2 else [a2[i]  for i in range(0, l2 - l1)]
    
    l = len(left)
    left_res = [0] * l
    for i in range(-1, -1-l, -1):
        res = left[i] + carry
        (carry, left_res[i]) = (1, res - 10) if res >= 10 else (0, res)
    
    left_res = left_res if carry == 0 else [carry] + left_res
    return left_res + partial_res
  
   
def multiply1(num1, num2):
    
    l1 = len(num1)
    l2 = len(num2)
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1 
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])
    shift = 0
    final_res = []    
    for i in range(-1, -1 - l1, -1):
        carry = 0
        curr_stage_res = [0] * l2 
        for j in range(-1, -1 - l2, -1):
            res = num1[i] * num2[j] + carry
            (carry, curr_stage_res[j]) = (res // 10, res % 10) if res >= 10 else (0, res)
            
        curr_stage_res = curr_stage_res if carry == 0 else [carry] + curr_stage_res
        final_res = add(curr_stage_res + [0] * shift, final_res)
        shift += 1
    
    
    #Remove Leading 0
    first_elem  = [i for i, x in enumerate(final_res) if x != 0]
    final_res = [0] if len(first_elem) == 0 else  final_res[first_elem[0]:]
    
    final_res = [sign * final_res[0]] + final_res[1:]
    return final_res

#Shorter version from the book    
def multiply2(num1, num2):
    res = [0] * (len(num1) + len(num2))
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1 
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    for i in reversed(range(len(num1))):
         for j in reversed(range(len(num2))):
             res[i + j + 1] += num1[i] * num2[j]
             res[i + j] += res[i + j + 1] // 10
             res[i + j + 1] %= 10 
    
    first_elem  = [i for i, x in enumerate(res) if x != 0]
    res = [0] if len(first_elem) == 0 else  res[first_elem[0]:]
    
    res = [sign * res[0]] + res[1:]
    return res

#TODO: Pad a number with zeros to make it of length power of 2 and try implementing
#Karatsuba method

def multiply(num1, num2):
    return multiply2(num1, num2)


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(generic_test.generic_test_main('int_as_array_multiply.tsv', multiply))
    
