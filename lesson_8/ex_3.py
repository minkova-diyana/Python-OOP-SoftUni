class vowels:
    def __init__(self, text: str):
        self.text = text
        vowels = 'aeiuyo'
        self.only_vowel_text = [l for l in self.text if l.lower() in vowels]
        self.start = 0
        self.end = len(self.only_vowel_text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        current = self.start
        if self.start <= self.end:
            self.start += 1
            return self.only_vowel_text[current]
        raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
