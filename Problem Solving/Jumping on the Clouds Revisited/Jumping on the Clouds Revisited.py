#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy = 100
    if c[0] == 1:
        energy -= 2
    for i in range(10000):
        energy -= 1
        if (k * (i + 1)) % len(c) == 0:
            break
        if c[(k * (i + 1)) % len(c)] == 1:
            energy -= 2
    return energy


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()