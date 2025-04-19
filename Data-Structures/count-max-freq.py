#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    count = Counter(arr)
    max_freq = max(count.values())

    most_frequent_birds = [bird for bird, freq in count.items() if freq == max_freq]
    return min(most_frequent_birds)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
