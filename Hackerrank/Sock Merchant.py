#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dict = {}
    for i in ar:
        if(i in dict):
            dict[i]+=1
        else:
            dict[i]=1
    f = 0
    for i in dict:
        if(dict[i]%2 == 0):
            f += dict[i]/2

        else:
            f += (dict[i]-1)/2
        
    return f



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = int(sockMerchant(n, ar))

    fptr.write(str(result) + '\n')

    fptr.close()
