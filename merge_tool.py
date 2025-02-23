# the problem is to split the string into k parts and remove the duplicate characters in each part
# The function merge_the_tools takes two arguments, a string s and an integer k
# The function splits the string into k parts and removes duplicate characters in each part
# The function prints the processed substring

def merge_the_tools(s, k):
    for i in range(0, len(s), k):  # Iterate over the string in chunks of size k
        substring = s[i:i+k]       # Extract the substring
        seen = set()               # Track seen characters
        unique_substring = ""      # Store unique characters
        
        for char in substring:     # Iterate over the substring
            if char not in seen:   # If character is not already seen
                seen.add(char)     # Mark character as seen
                unique_substring += char  # Add to unique substring
        
        print(unique_substring)    # Print the processed substring

# Sample usage
s = "AABCAAADA"
k = 3
merge_the_tools(s, k)
