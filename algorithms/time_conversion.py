#!/bin/python3

import os
from datetime import datetime


# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.


# A clean solution using datetime module
def timeConversion(s):
    dt = datetime.strptime(s, '%I:%M:%S%p')
    return dt.strftime('%H:%M:%S')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()