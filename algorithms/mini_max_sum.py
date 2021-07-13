#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.


def miniMaxSum(arr):
    _total, _min, _max = 0, float('inf'), float('-inf')
    
    for num in arr:
        _total += num
        _min = min(num, _min)
        _max = max(num, _max)
    
    print(_total - _max, _total - _min)

    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)