# Problem Stmt.:
# Given an array of integers, return a new array such that each element at index i of the new
# array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

#from functools import reduce
from math import log10

def solve(arr):
    #using division
    #product = reduce((lambda x,y:x*y),arr)
    #res = list(map((lambda x: product//x),arr))

    #without using division - 1
    #res = [1]*len(arr)
    #prod_so_far = 1
    #for i in range(0,len(arr)):
    #    res[i] = prod_so_far
    #    prod_so_far *= arr[i]
    #prod_so_far = 1
    #for i in range(len(arr)-1,-1,-1):
    #    res[i] *= prod_so_far
    #    prod_so_far *= arr[i]

    #without using division - 2
    res = []
    sum_of_logs = 0
    eps = 1e-9
    for i in arr:
        sum_of_logs += log10(i)
    for i in arr:
        res.append(int(eps+pow(10,sum_of_logs-log10(i))))
    return res

if __name__ == "__main__":
    arr1,arr2 = [1,2,3,4,5],[3,2,1]
    print(solve(arr1))
    print(solve(arr2))
