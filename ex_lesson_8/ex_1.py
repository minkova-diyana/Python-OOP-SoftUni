class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.start_count = 0
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        current = self.start
        if self.start_count < self.count:
            self.start_count += 1
            self.start += self.step
            return current
        raise StopIteration()

numbers = take_skip(2, 6)
for number in numbers:
    print(number)
numbers = take_skip(10, 5)
for number in numbers:
    print(number)

