# Problem Stmt.:
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

def firstPositiveMissingInt(arr):
    for i in range(0,len(arr)):
        if (arr[i]<=0 or arr[i]>0):
            continue
        val = arr[i]
        while (arr[val-1]!=val):
            val,arr[val-1]=arr[val-1],val
            if (val<0 or val>len(arr)):
                break
    for i in range(0,len(arr)):
        if arr[i] != i+1:
            return i+1
    return len(arr)+1


if __name__ == "__main__":
    print(firstPositiveMissingInt([3,4,-1,1]))
    print(firstPositiveMissingInt([1,2,0]))
    print(firstPositiveMissingInt([0,10,2,-10,-20]))