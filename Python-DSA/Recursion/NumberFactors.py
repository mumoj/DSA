from mypy import *

def factorial(n):
    if n ==1 :
        return 1

    n -= 1

    return factorial(n) * factorial(n-1)

