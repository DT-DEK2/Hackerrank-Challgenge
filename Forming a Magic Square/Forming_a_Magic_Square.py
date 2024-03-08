# https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true
# Difficulty: Medium

#%%
import math
import os
import random
import re
import sys
import itertools



#%%
def formingMagicSquare(s):

    # all possible 3x3 magic squares
    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]

    # flatten the input 3x3 matrix
    s = list(itertools.chain(*s))

    # calculate the cost of converting the input matrix to each of the magic squares
    costs = []
    for magic_square in magic_squares:
        cost = 0
        for i, j in zip(s, magic_square):
            cost += abs(i - j)
        costs.append(cost)

    # return the minimum cost
    return min(costs)


if __name__ == '__main__':
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(result)

