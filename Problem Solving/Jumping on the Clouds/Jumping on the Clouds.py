#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    position = 0
    counter = 0
    while True:
        if position >= len(c) - 1:
            break
        try:
            if c[position + 2] == 0:
                position += 2
                counter += 1
            else:
                position += 1
                counter += 1
        except IndexError:
            counter += 1
            break
    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()