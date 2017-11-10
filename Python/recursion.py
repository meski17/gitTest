def fib(n):
    if n >= 2:
        return fib(n-1) + fib(n-2)
    return n


# for i in range(1, 30):
#    print(i+1, ":", fib(i))


fibonacci_cache = {}


def fibnonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibnonacci(n-1) + fibnonacci(n-2)
    fibonacci_cache[n] = value
    return value


for i in range(1, 101):
    print(i+1, ":", fibnonacci(i))
