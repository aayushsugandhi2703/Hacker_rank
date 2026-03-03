import re

n = int(input())

pattern = r'(?<=\s)&&(?=\s)|(?<=\s)\|\|(?=\s)'

for _ in range(n):
    line = input()
    
    def replace_op(match):
        if match.group() == '&&':
            return 'and'
        else:
            return 'or'
    
    result = re.sub(pattern, replace_op, line)
    print(result)

    '''
    explaination for regex pattern:
    
    (?<=\s) - Positive lookbehind assertion that ensures the preceding character is a whitespace
    (?=\s) - Positive lookahead assertion that ensures the following character is a whitespace
    && - Matches the '&&' operator
    \|\| - Matches the '||' operator
    
    '''