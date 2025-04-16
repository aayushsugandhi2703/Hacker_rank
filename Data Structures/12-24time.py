#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    hr = int(s[0:2])
    mi = int(s[3:5])
    se = int(s[6:8])
    n = s[8:].upper()
    
    if n == 'AM':
        if hr == 12:
            hr =0
    if n == 'PM':
        if hr != 12:
            hr = hr+12
    return f'{hr:02d}:{mi:02d}:{se:02d}'    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
