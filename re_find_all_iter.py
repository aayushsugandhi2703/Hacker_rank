import re

s = input().strip()
pattern = r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])'

matches = re.finditer(pattern, s)

results = [match.group(1) for match in matches]
if results:
    print("\n".join(results))
else:
    print("-1")