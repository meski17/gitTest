from functools import lru_cache


@lru_cache(maxsize=1000)
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n-1) + fib(n-2)
    return n


for n in range(1, 501):
    print(n, ":", fib(n))
