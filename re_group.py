# this question tells about solving the problem using regular expression
# The problem is to find the first recurring character in the string
import re

s = input().strip()  

match = re.search(r'([a-zA-Z0-9])(\1)', s)  
print(match.group(1) if match else -1)