""" 
Given an array of integers ans a sum, the task is to count all subsets of given array with sum equal to given sum.

Input:
n = # Size of an array
arr = # array elements
sum = # sum value

Output:
Count all the subsets of given array with sum equal to given sum.

Example:
Input:
6
2 3 5 6 8 10
10
output:
3
"""
"""Solution"""

from itertools import combinations
def subsets(n,arr, s):
    subsets_list = []
    count = 0
    for i in range(n+1):
        subsets_list.extend(combinations(arr,i))
    for j in subsets_list:
        if (sum(j) == s):
            count += 1
            print(j)
    return count
output = subsets(6,[2,3,5,6,8,10],10)
print(output)
        