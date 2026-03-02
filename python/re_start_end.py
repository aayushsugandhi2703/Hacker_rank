import re
s1 =input().strip()
s2 =input().strip()
pattern = f'(?=({re.escape(s2)}))'
matches = list(re.finditer(pattern, s1))
if not matches:
    print("(-1, -1)")
else:
    for match in matches:
        start = match.start()
        end = start + len(s2) - 1  # Calculate correct end index
        print(f"({start}, {end})")