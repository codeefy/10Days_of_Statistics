# https://www.hackerrank.com/challenges/s10-quartiles/problem?isFullScreen=true
# Objective
# In this challenge, we practice calculating quartiles. Check out the Tutorial tab for learning materials and an instructional video!
# Task
# Given an array, , of  integers, calculate the respective first quartile (), second quartile (), and third quartile (). It is guaranteed that , , and  are integers.
# Input Format
# The first line contains an integer, , denoting the number of elements in the array.
# The second line contains  space-separated integers describing the array's elements.
# Constraints
# , where  is the  element of the array.
# Output Format
# Print  lines of output in the following order:
# The first line should be the value of .
# The second line should be the value of .
# The third line should be the value of .
# Sample Input  
# 9
# 3 7 8 5 12 14 21 13 18
# Sample Output
# 6
# 12
# 16
import os 

def quartiles(arr):
    # Sort the array
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    
    # Helper function to calculate median
    def median(sub_arr):
        sub_n = len(sub_arr)
        mid = sub_n // 2
        if sub_n % 2 == 0:
            return (sub_arr[mid - 1] + sub_arr[mid]) // 2
        else:
            return sub_arr[mid]
    
    # Calculate Q1
    Q1 = median(sorted_arr[:n//2])
    
    # Calculate Q2 (median of the entire array)
    Q2 = median(sorted_arr)
    
    # Calculate Q3
    if n % 2 == 0:
        Q3 = median(sorted_arr[n//2:])
    else:
        Q3 = median(sorted_arr[n//2 + 1:])
    
    return [Q1, Q2, Q3]

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    #fptr.write('\n'.join(map(str, res)))
    #fptr.write('\n')

    #fptr.close()
