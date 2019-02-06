# Problem Stmt.:
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

# def non_adjacent_largest_sum(arr):
#     if len(arr) == 1:
#         return arr[0]
#     elif len(arr) == 2:
#         return max(arr[0],arr[1])
#     else:
#         return max(non_adjacent_largest_sum(arr[:len(arr)-1]),arr[-1]+non_adjacent_largest_sum(arr[:len(arr)-2]))

# mem = []
# def non_adjacent_largest_sum(arr):
#     global mem
#     if len(arr) == 1:
#         return arr[0]
#     if len(arr) == 2:
#         return max(arr[0],arr[1])
#     if len(arr) in mem:
#         return mem[len(arr)]
#     mem.append(max(non_adjacent_largest_sum(arr[:len(arr)-1]),arr[-1]+non_adjacent_largest_sum(arr[:len(arr)-2])))
#     return mem[-1]

def non_adjacent_largest_sum(arr):
    prevOne = prevTwo = res = 0
    for i in range(len(arr)):
        if i == 0:
            res = arr[0]
        elif i == 1:
            res = max(arr[0],arr[1])
        else:
            res = max(prevOne,arr[i] + prevTwo)
        prevTwo = prevOne
        prevOne = res
    return res

if __name__ == "__main__":
    print(non_adjacent_largest_sum([2, 4, 6, 2, 5]))
    print(non_adjacent_largest_sum([5, 1, 1, 5]))