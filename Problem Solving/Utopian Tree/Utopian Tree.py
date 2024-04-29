#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    suma = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            suma += 1
        else:
            suma *= 2
    return suma


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()