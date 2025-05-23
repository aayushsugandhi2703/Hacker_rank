#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Remove the pair
        else:
            stack.append(char)
    
    result = ''.join(stack)
    return result if result else "Empty String"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
