#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    maximum = scores[0]
    minimum = scores[0]
    max_records = 0
    min_records = 0
    for i in scores:
        if i > maximum:
            maximum = i
            max_records += 1
        elif i < minimum:
            minimum = i
            min_records +=1
    return [max_records, min_records]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()