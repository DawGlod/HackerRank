#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    results = []
    for i in range(p, q + 1):
        i_square = str(i ** 2)
        i = str(i)
        length = len(i)
        i = int(i)
        l, r = i_square[:-length], i_square[-length:]
        if l:
            l = int(l)
            r = int(r)
            if l + r == i:
                results.append(i)
        else:
            r = int(r)
            if r == i:
                results.append(i)
    if len(results) == 0:
        print("INVALID RANGE")
    else:
        print(*results)


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)