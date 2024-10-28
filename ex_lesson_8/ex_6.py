def fibonacci():
    n = 0
    m = 1
    while True:
        yield n
        n, m = m, n + m


generator = fibonacci()
for i in range(10):
    print(next(generator))
