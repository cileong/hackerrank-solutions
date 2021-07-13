#!/bin/python3

import os


# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.


# Solution 1
# More readable but slower (two-pass)
def birthdayCakeCandles(candles):
    return candles.count(max(candles))


# Solution 2
# Less readable but faster (one-pass)
def birthdayCakeCandles(candles):
    _max, freq = 0, 0
    for num in candles:
        if num > _max:
            _max = num
            freq = 1
        elif num == _max:
            freq += 1
    return freq
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()