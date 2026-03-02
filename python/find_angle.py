import math

# Read input values
a = int(input().strip())
b = int(input().strip())

# Calculate angle in degrees
angle = math.degrees(math.atan(a / b))

# Round to the nearest integer
ans = round(angle)
e = chr(176)
print(f"{ans}{e}")
