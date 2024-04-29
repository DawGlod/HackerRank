#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    my_dict = {}
    for i in arr:
        if i not in my_dict:
            my_dict.update({i: 1})
        else:
            my_dict[i] += 1
    highest_value = max(my_dict.values())
    list_of_maxes = [number for number in my_dict if my_dict[number] == highest_value]
    return min((list_of_maxes))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()