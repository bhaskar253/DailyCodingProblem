# Problem Stmt.:
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

def checkTwoSum(arr, k):
    hMap = {}
    for item in arr:
        difference = k-item
        if difference not in hMap:
            hMap[item] = difference
        else:
            return True
    return False

if __name__ == "__main__":
    arr = [7,15,13,2,10]
    k = 21
    print(checkTwoSum(arr,k))
