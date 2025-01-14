def cache(func):
    log = {}

    def wrapper(*args, **kwargs):
        if args[0] not in log:
            log[args[0]] = func(*args, **kwargs)
        return log[args[0]]

    wrapper.log = log
    return wrapper



@cache
def fibonacci(n):
    if n < 2:

        return n

    else:

        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
fibonacci(4)
print(fibonacci.log)
