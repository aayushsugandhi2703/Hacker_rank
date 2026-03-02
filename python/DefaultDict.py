from collections import defaultdict

# Read n and m
n, m = map(int, input().split())

# Dictionary to store positions of words in Group A
word_positions = defaultdict(list)

# Read Group A words and store their positions
for i in range(1, n + 1):  # 1-based index
    word = input().strip()
    word_positions[word].append(i)

# Read Group B words and output positions
for _ in range(m):
    word = input().strip()
    if word in word_positions:
        print(" ".join(map(str, word_positions[word])))  # Print positions space-separated
    else:
        print("-1")  # If word not found in Group A
