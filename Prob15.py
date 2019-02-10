# Problem Stmt.:
# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
from random import randrange

def resorvoirSampling(stream,k):
    res = [0]*k
    for i,e in enumerate(stream):
        if i==k:
            break
        res[i] = e
    for i,item in enumerate(stream):
        j = randrange(i+1)
        if j < k:
            res[j] = item
    return res

def pickRandom(stream):
    return resorvoirSampling(stream,1)

if __name__ == "__main__":
    stream = range(1,5)
    print(*pickRandom(stream))
