#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    my_dict = {}
    for i in a:
        if i not in my_dict:
            my_dict.update({i: 1})
        else:
            my_dict[i] += 1
    possibilities = [i for i in my_dict if my_dict[i] % 2 == 0]
    results = []
    for i in range(len(possibilities)):
        helper = -1
        for j in range(len(a)):
            if a[j] == possibilities[i]:
                if helper == -1:
                    helper = j
                else:
                    results.append(j - helper)
                    break
    if not results:
        return -1
    return min(results)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()