#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # preparing hour
    hours, minutes, seconds = s.split(":")
    ampm = seconds[2] + seconds[3]
    seconds = seconds[0] + seconds[1]
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    # converting to 24h
    if ampm == "AM" and hours < 12:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    if ampm == "AM" and hours == 12:
        return f"{hours - 12:02d}:{minutes:02d}:{seconds:02d}"
    elif ampm == "PM" and hours < 12:
        return f"{hours + 12:02d}:{minutes:02d}:{seconds:02d}"
    elif ampm == "PM" and hours == 12:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()