s = input()
print(any(c.isalnum() for c in s))  # At least one alphanumeric character
print(any(c.isalpha() for c in s))  # At least one alphabetic character
print(any(c.isdigit() for c in s))  # At least one digit
print(any(c.islower() for c in s))  # At least one lowercase character
print(any(c.isupper() for c in s))  # At least one uppercase character
