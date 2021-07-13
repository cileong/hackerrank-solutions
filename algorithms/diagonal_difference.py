#!/bin/python3

import os

# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

def diagonalDifference(arr):
    dim = len(arr)
    primary_diag, secondary_diag = 0, 0
    
    for i in range(dim):
        primary_diag += arr[i][i]
        secondary_diag += arr[i][-(i+1)]
    
    return abs(primary_diag - secondary_diag)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
