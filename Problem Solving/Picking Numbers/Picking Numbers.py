#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a = sorted(a)
    my_dict = {}
    for i in a:
        if i not in my_dict:
            my_dict.update({i: 1})
        else:
            my_dict[i] += 1
    my_keys = list(my_dict.keys())
    my_values = list(my_dict.values())
    if len(my_values) == 1:
        return n
    maxi = 0
    for i in range(len(my_values) - 1):
        if my_values[i] > maxi:
            maxi = my_values[i]
        if (my_values[i] + my_values[i+1] > maxi and abs(my_keys[i] - my_keys[i+1]) == 1):
            maxi = my_values[i] + my_values[i+1]
    return maxi

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()