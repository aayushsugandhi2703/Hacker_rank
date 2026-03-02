import re
import email.utils

n = int(input())
pattern = r'^[a-z](\w|-|\.)*@[a-z]+\.[a-z]{1,3}$'

for i in range(n): 
    email_string = input()
    email_string_to_check = (email.utils.parseaddr(email_string))
    if re.search(pattern, str(email_string_to_check[1])):
        print(email_string)
