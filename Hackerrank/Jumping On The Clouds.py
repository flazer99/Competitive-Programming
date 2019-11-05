#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c,n):
    f=0
    i=0
    while(i<n):
        if(i==n-1):
            break
        else:
            if(i+2<n):
                if(c[i+2]==0):
                    f+=1
                    i+=2
                elif(c[i+1]==0 and c[i+2]==1):
                    f+=1
                    i+=1
            else:
                f+=1
                i+=1

    # for i in range(n):
       
    return f
      
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c,n)

    fptr.write(str(result) + '\n')

    fptr.close()
