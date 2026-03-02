# the problem was to check if the given regex pattern is valid or not
# the solution is to use the re module in python to compile the pattern and check if it raises an error or not

import re

def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False

# Read number of test cases
n = int(input())

# Loop through each test case
for _ in range(n):
    pattern = input().strip()
    print(is_valid_regex(pattern))
