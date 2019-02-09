# Problem Stmt.:
# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
# Hint: The basic equation of a circle is x2 + y2 = r2.
from random import random

def monte_carlo_simulation(n=2):
    nm = dm = pi = 0
    interval = 10000000
    while dm<=interval:
        x = random()
        y = random()
        if x*x + y*y <= 1:
            nm += 1
        dm += 1
        pi = 4*nm/dm
    return str(pi)[:2+n]

if __name__ == "__main__":
    print(monte_carlo_simulation(3))