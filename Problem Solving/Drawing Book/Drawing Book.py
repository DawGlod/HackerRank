#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    page = 1
    counter_forwards = 0
    if p != 1:
        for i in range(n // 2):
            counter_forwards += 1
            page += 2
            if page >= p:
                break
    page = n
    counter_backwards = 0
    if p != n and n % 2 == 0:
        for i in range(n // 2):
            counter_backwards += 1
            page -= 2
            if page <= p:
                break
    elif p != n and p != n - 1:
        page -= 1
        for i in range(n // 2):
            counter_backwards += 1
            page -= 2
            if page <= p:
                break
    results = [counter_forwards, counter_backwards]
    return min(results)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()