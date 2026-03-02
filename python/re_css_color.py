import re 

N = int(input())

hex_code = r'(?<=[:\s])#[A-Fa-f0-9]{3,6}(?!\w)'

css_colors = []

for _ in range(N):
    line = input()
    css_colors.extend(re.findall(hex_code, line))
    
print('\n'.join(css_colors)) 
    