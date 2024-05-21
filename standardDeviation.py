#!/bin/python3
# https://www.hackerrank.com/challenges/s10-standard-deviation/problem?isFullScreen=false



import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(vals):
    # Print your answers to 1 decimal place within this function
    n=len(vals) #calculate the lenght of arry
    mean=sum(vals)/n #calculate mean of arr using sum function then divide them to n 
    squar_diff=[(x-mean)**2 for x in vals] # calculate the squared distance from the mean 
    variance=sum(squar_diff)/n #calculate the variance 
    #now calcuate the standard deviation 
    std_dev=math.sqrt(variance)
    print(f'{std_dev:.1f}') #round up to 1 decimal 
    
if __name__ == '__main__':
    
    n = int(input().strip())#input from user 

    vals = list(map(int, input().rstrip().split())) #

    stdDev(vals)
