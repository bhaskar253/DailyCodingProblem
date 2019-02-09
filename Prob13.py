# Problem Stmt.:
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

from collections import Counter

# def getLongestSubstring(str,k):
#     storage = set()
#     stack = [str]
#     while len(stack)>0:
#         curr = stack.pop()
#         if len(curr) < k:
#             continue
#         if len(Counter(curr)) == k:
#             storage.add(curr)
#         stack.append(curr[1:len(curr)])
#         stack.append(curr[0:len(curr)-1])
#     return max(map(lambda s: len(s),storage))

def getLongestSubstring(str,k):
    if not str or len(str) == 0 or k<=0:
        #return (str,False)
        return 0
    b = e = bs = es = 0
    myDict = {}
    while e<len(str):
        if (len(myDict) < k and str[e] not in myDict) or (len(myDict)<=k and str[e] in myDict):
            if e-b > es-bs:
                bs,es = b,e
            myDict[str[e]] = 1 if str[e] not in myDict else myDict[str[e]] + 1
            e += 1
        else:
            myDict[str[b]] -= 1
            if myDict[str[b]] == 0:
                myDict.pop(str[b])
            b += 1
    #return (str[bs:es+1],True)
    return es-bs+1

if __name__ == "__main__":
    print(getLongestSubstring("abcba",2))