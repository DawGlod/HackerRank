#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    suma = 1
    for i in range(2, n + 1):
        suma *= i
    print(suma)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)