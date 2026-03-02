def pattern(M, N):
    # Top half
    for i in range(M // 2):
        print("-" * ((N - (2 * i + 1) * 3) // 2) + ".|." * (2 * i + 1) + "-" * ((N - (2 * i + 1) * 3) // 2))

    # Middle "WELCOME"
    print("-" * ((N - 7) // 2) + "WELCOME" + "-" * ((N - 7) // 2))

    # Bottom half (mirror of the top)
    for i in range(M // 2 - 1, -1, -1):
        print("-" * ((N - (2 * i + 1) * 3) // 2) + ".|." * (2 * i + 1) + "-" * ((N - (2 * i + 1) * 3) // 2))

# Take input
m = int(input())  # M (height) must be odd
n = 3 * m         # N (width)
pattern(m, n)
