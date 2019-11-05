#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    f = 0
    # list1 = list(s)
    # str1=""
    # for i in range(n):
    #     j = i%len(s)
    #     str1 += list1[j]
    #     if(list1[j]=='a'):
    #         f+=1
    for i in s:
        if(i=='a'):
            f += 1

    quot = n//len(s)
    f = f*quot
    rem = n%len(s)
    r = 0
    for i in range(rem):
        if(s[i]=='a'):
            r+=1

    return f + r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
