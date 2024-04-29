#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    list_of_cuts = []
    my_set = set(arr)
    for i in range(len(my_set)):
        counter = 0
        minimum = min(arr)
        for j in range(len(arr)):
            if arr[j] == 1001:
                continue
            arr[j] -= minimum
            counter += 1
            if arr[j] == 0:
                arr[j] = 1001
        list_of_cuts.append(counter)
    return list_of_cuts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()