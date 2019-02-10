# Problem Stmt.
# You run an e-commerce website and want to record the last N order ids in a log. 
# Implement a data structure to accomplish this, with the following API:
# •	record(order_id): adds the order_id to the log
# •	get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.

from collections import deque

class OrdersLog:
    def __init__(self, cache_size=10):
        self.cache_size = cache_size
        self.cache = deque(maxlen = self.cache_size)
    def record(self,order_id):
        if len(self.cache)>self.cache_size:
            self.cache.popleft()
        self.cache.append(order_id)
    def get_last(self,i):
        return self.cache[-i]

if __name__ == "__main__":
    log = OrdersLog(5)
    for i in range(4):
        log.record(f'ORD#{i+1}')
    print(log.get_last(4))
