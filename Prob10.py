# Problem Stmt.:
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import time

def job_scheduler(function, wait_before_call_in_ms):
    time.sleep(wait_before_call_in_ms/1000)
    function()

if __name__ == "__main__":
    print('Start Time: ' + str(time.ctime()))
    job_scheduler(lambda: print('Hello'),5000)
    print('End Time: ' + str(time.ctime()))