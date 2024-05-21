
#https://www.hackerrank.com/challenges/s10-interquartile-range/problem?isFullScreen=true
#Objective
#In this challenge, we practice calculating the interquartile range. We recommend you complete the Quartiles challenge before attempting this problem.
#Task
#The interquartile range of an array is the difference between its first () and third () quartiles (i.e., ).
#Given an array, , of  integers and an array, , representing the respective frequencies of 's elements, construct a data set, , where each  occurs at frequency . Then calculate and print 's interquartile range, rounded to a scale of  decimal place (i.e.,  format).
#Tip: Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets.
#Input Format
#The first line contains an integer, , denoting the number of elements in arrays  and .
#The second line contains  space-separated integers describing the respective elements of array .
#The third line contains  space-separated integers describing the respective elements of array .
#Constraints

#The number of elements in  is equal to .
#Output Format
#Print the interquartile range for the expanded data set on a new line. Round your answer to a scale of  decimal place (i.e.,  format).
#Sample Input
#6
#6 12 8 10 20 16
#5 4 3 2 1 5
#Sample Output
#9.0
#Explanation
#The given data is:
#X = [6, 12, 8, 10, 20, 16]
#F = [5, 4, 3, 2, 1, 5]
#First, we create data set  containing the data elements and their frequencies:
#S = [6, 6, 6, 6, 6, 12, 12, 12, 12, 8, 8, 8, 10, 10, 20, 16, 16, 16, 16, 16]
#As there are an even number of data points, we will split this data set into two halves:
#L = [6, 6, 6, 6, 6, 8, 8, 8, 10, 10]
#U = [12, 12, 12, 12, 16, 16, 16, 16, 16, 20]
#The lower quartile is the median of the lower half of the data set:
#Q1 = 6 + 8 / 2 = 7
#The upper quartile is the median of the upper half of the data set:
#Q3 = 16 + 16 / 2 = 16
#The interquartile range is Q3 - Q1 = 16 - 7 = 9
#When rounded to a scale of  decimal place, we get  as our final answer.
def interQuartile(values, freqs):
    # Create the data set S
    S = [] 
    for i in range(len(values)):
        S += [values[i]] * freqs[i]

    S = sorted(S)
    n = len(S)

    def median(sub_arr):
        sub_n = len(sub_arr)
        mid = sub_n // 2
        if sub_n % 2 == 0:
            return (sub_arr[mid - 1] + sub_arr[mid]) / 2.0
        else:
            return sub_arr[mid]

    # Calculate Q1
    lower_half = S[:n // 2]
    Q1 = median(lower_half)
    
    # Calculate Q3
    if n % 2 == 0:
        upper_half = S[n // 2:]
    else:
        upper_half = S[(n // 2) + 1:]
    Q3 = median(upper_half)

    # Print the interquartile range to 1 decimal place
    print(f"{Q3 - Q1:.1f}")

if __name__ == '__main__':
    n = int(input().strip())
    values = list(map(int, input().rstrip().split()))
    freqs = list(map(int, input().rstrip().split()))

    # Ensure that the number of elements in S is equal to the sum of freqs
    assert len(values) == len(freqs), "The length of values and freqs must be the same"
    assert sum(freqs) <= 1000, "The sum of frequencies must be less than or equal to 1000"

    interQuartile(values, freqs)
