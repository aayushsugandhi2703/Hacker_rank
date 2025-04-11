'''
^(?!.*(\d)(-?\1){3})[4-6]\d{3}(-?\d{4}){3}$

This regex is used to validate a specific format of a string, which is likely related to a credit card number or similar numeric sequence. Let's break it down step by step:
1. ^ → Asserts the start of the string.
2. (?!.*(\d)(-?\1){3}) → This is a negative lookahead assertion.
    It checks that the string does not contain a sequence of four or more consecutive repeated digits, which can be separated by hyphens (-?).
3. [4-6] → The first digit must be between 4 and 6.
4. \d{3} → The next three digits can be any digit (0-9).
5. (-?\d{4}){3} → This part matches three groups of four digits, which can also be separated by hyphens (-?).
6. $ → Asserts the end of the string.

Breaking this part:
.*(\d) → find any digit (\d) anywhere in the string and remember it.

(-?\1){3} → checks if that same digit appears three more times ({3}) after it, optionally separated by hyphens (-?).

📌 So this prevents 4 or more consecutive repeated digits, e.g.:

1111, 2222, 5-5-5-5, etc. — ❌ Invalid.

Allowed:

1234, 5-5-5-6, 9-9-9-0, etc.
'''

import re

pattern = r'^(?!.*(\d)(-?\1){3})[4-6]\d{3}(-?\d{4}){3}$'

n = int(input())

for _ in range(n):
    card = input().strip()
    if re.fullmatch(pattern, card):
        print("Valid")
    else:
        print("Invalid")
