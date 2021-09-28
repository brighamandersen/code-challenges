#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

# See https://www.hackerrank.com/challenges/2d-array/problem for details

def hourglassSum(arr):
    sums = []
    
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr) - 1):
            topSection = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
            midSection = arr[i][j]
            bottomSection = arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            currentSum = topSection + midSection + bottomSection
            sums.append(currentSum)
    return max(sums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
