#!/bin/python3


# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.


def plusMinus(arr):
    n = len(arr)
    neg, zero, pos = 0, 0, 0
    
    for num in arr:
        if num < 0:
            neg += 1
        elif num == 0:
            zero += 1
        else:
            pos += 1
    
    print(pos/n, neg/n, zero/n, sep='\n')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)