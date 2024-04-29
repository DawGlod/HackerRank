#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    maximum = max(arr)
    minimum = min(arr)
    sum_all = 0
    for i in arr:
        sum_all += i
    print(f"{sum_all - maximum} {sum_all - minimum}")


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)