#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    a = sorted(a)
    b = sorted(b)
    highest_a = a[-1]
    lowest_b = b[0]
    if highest_a > lowest_b:
        return 0
    possibilities = set()
    for i in range(lowest_b // highest_a):
        for j in range(len(a)):
            if (highest_a * (i + 1)) % a[j] == 0:
                possibilities.add(highest_a * (i + 1))
            else:
                if highest_a * (i + 1) in possibilities:
                    possibilities.remove(highest_a * (i + 1))
                break
    sum_all = len(possibilities)
    for i in possibilities:
        for j in range(len(b)):
            if b[j] % i != 0:
                sum_all -= 1
                break
    return sum_all

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()