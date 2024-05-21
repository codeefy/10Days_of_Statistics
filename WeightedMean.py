#weighted mean 
#https://www.hackerrank.com/challenges/s10-weighted-mean/problem?isFullScreen=true

import math
import os
import random
import re
import sys

# Complete the 'weightedMean' function below

def weightedMean(X, W):
    weighted_sum = sum([X[i] * W[i] for i in range(len(X))])
    sum_weights = sum(W)
    return weighted_sum / sum_weights

if __name__ == '__main__':
    n = int(input().strip())

    X = list(map(int, input().rstrip().split()))

    W = list(map(int, input().rstrip().split()))

    result = weightedMean(X, W)
    print("{:.1f}".format(result))