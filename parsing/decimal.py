import re

def validate_decimal(number):
    pattern = r'^[+-.]?\d*\.\d+$'
    return bool(re.fullmatch(pattern, number))

if __name__ == '__main__':
    size = int(input())
    for i in range(size):
        num = input()
        print(validate_decimal(num))    

'''
explaination for regex pattern:

^ - start of the string
[+-.]? - checks if starts with only =,-,. or nothing from this set
\d* - zero or more digits before the decimal point
\. - literal decimal point
\d+ - one or more digits after the decimal point
$ - end of the string

'''