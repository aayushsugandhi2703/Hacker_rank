'''
Given an array A of length N. Alex and Bob have decided to play a game called 'Take it apart' 
At the beginning of the game, players pick a side of the array, that is, either the start (S) or the end (E) of the array, 
and it's fixed for the rest of the game. Then, they start playing in turns. Alex goes first. 
They pick a number from their side and remove the number from the array. This number is considered collected by the respective player.
Task
Your task is to calculate the minimum absolute difference between the sum of collected numbers by Alex and Bob.
Function description
Complete the function solve provided in the editor. This function takes the following two parameters and returns the required answer:
﻿﻿N: Represents the size of the array A
﻿﻿A: Represents the numbers in the array A

Note: This is the input format that you must use to provide custom input (available above the Compile and Test button).
﻿﻿The first line contains T, denoting the number of test cases. T also specifies the number of times you have to run the solve function on a different set of inputs.
﻿﻿For each test case:
﻿﻿The first line contains N, which denotes the size of the array A
﻿﻿The second line contains N integers denoting the array A.
Output format For each test case, print the required answer on a new line.
Constraints
1≤T ≤ 1000
'''
def play_game(N, A, alex_side, bob_side):
    left = 0
    right = N - 1
    alex_sum = 0
    bob_sum = 0
    turn = 0  # 0 means Alex's turn, 1 means Bob's turn
    
    while left <= right:
        if turn == 0:  # Alex's turn
            if alex_side == 'S':
                alex_sum += A[left]
                left += 1
            else:  # 'E'
                alex_sum += A[right]
                right -= 1
        else:  # Bob's turn
            if bob_side == 'S':
                bob_sum += A[left]
                left += 1
            else:  # 'E'
                bob_sum += A[right]
                right -= 1
        
        turn ^= 1
    
    return abs(alex_sum - bob_sum)

def solve(N, A):
    scenarios = [
        ('S', 'S'),
        ('S', 'E'),
        ('E', 'S'),
        ('E', 'E')
    ]

    min_diff = float('inf')
    for alex_side, bob_side in scenarios:
        diff = play_game(N, A, alex_side, bob_side)
        min_diff = min(min_diff, diff)

    return min_diff

# Input handling
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    result = solve(N, A)
    print(result)
