class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.end = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        next_index = self.end
        if self.end >= 0:
            self.end -= 1
            return self.iterable[next_index]
        raise StopIteration()



reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
