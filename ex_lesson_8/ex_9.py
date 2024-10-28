from itertools import permutations


def possible_permutations(numbers: list):
    for group in permutations(numbers):
        yield list(group)


[print(n) for n in possible_permutations([1, 2, 3])]
print()
[print(n) for n in possible_permutations([1])]