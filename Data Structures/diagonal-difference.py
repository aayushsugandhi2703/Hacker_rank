def diagonalDifference(arr):
    lr = 0  # left-to-right diagonal sum
    rl = 0  # right-to-left diagonal sum
    n = len(arr)
    
    for i in range(n):
        lr += arr[i][i]
        rl += arr[i][n - 1 - i]
    
    return abs(lr - rl)
    