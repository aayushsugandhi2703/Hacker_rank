#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    l = len(arr)
    pc =0
    zc =0
    nc =0
    for i in arr:
        if (i>0):
            pc += 1
        elif (i<0):
            nc +=1
        else:
            zc +=1
    a = pc/l
    b = nc/l
    c = zc/l
    print(f"{a:.6f}")
    print(f"{b:.6f}")
    print(f"{c:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
