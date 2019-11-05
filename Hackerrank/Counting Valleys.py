#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    f = 0
    ctr = 0
    if(s[0]=='U'):
        f+=1
    else:
        f-=1
    for i in range(1,n):
        if(f==0 and s[i-1]=='U'):
            ctr+=1
        if(s[i]=='U'):
            f+=1
        else:
            f-=1
    
    if(f==0 and s[len(s)-1]=='U'):
        ctr+=1
    return ctr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
