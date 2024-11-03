#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    # primary diagonal
    pd = []
    for i in range(len(arr)):
        pd.append(arr[i][i])
    print(pd)
    p = sum(pd)
    # secondary diagonal
    sd = []
    for i,j in enumerate(range(len(arr)-1,-1,-1)):
        sd.append(arr[i][j])
    print(sd)
    s = sum(sd)
    print(s,p)
    diagonal_diff = abs(p - s)

    return diagonal_diff


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    # fptr.write(str(result) + '\n')
    # fptr.close()
    print(result)
