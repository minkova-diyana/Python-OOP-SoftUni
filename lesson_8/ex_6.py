def reverse_text(text: str):
    last_index = len(text) - 1
    first_index = 0
    while last_index >= first_index:
        yield text[last_index]
        last_index -= 1


for char in reverse_text("step"):
    print(char, end='')
