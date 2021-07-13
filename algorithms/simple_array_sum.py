#!/bin/python3

import os

# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.

# Solution 1:
# def simpleArraySum(ar):
#     res = 0
#     for i in ar:
#         res += i
#     return res


# Solution 2:
def simpleArraySum(ar):
    return sum(ar)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    fptr.write(str(result) + '\n')

    fptr.close()