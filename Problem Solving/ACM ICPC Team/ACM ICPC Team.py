#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    results = []
    for i in range(len(topic) - 1):
        for j in range(i, len(topic) - 1):
            results.append(str(int(topic[i]) + int(topic[j + 1])))
    result_in_nums = []
    for i in results:
        result_in_nums.append(i.count("1") + i.count("2"))
    maximum = max(result_in_nums)
    counter = result_in_nums.count(maximum)
    return [maximum, counter]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()