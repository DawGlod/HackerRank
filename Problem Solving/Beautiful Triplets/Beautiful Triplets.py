#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    counter = 0
    results = []
    for i in range(len(arr) - 2):
        for j in range(i, len(arr) - 2):
            if arr[j+1] - arr[i] == d:
                for k in range(i, len(arr) - 2):
                    if arr[k+2] - arr[j+1] == d:
                        results.append([arr[i], arr[j+1], arr[k+2]])
    print(results)
    return len(results)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
