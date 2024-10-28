from math import ceil


class PhotoAlbum:
    SLOT_COUNT = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for r in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        row_count = ceil(photos_count / cls.SLOT_COUNT)
        return cls(row_count)

    def add_photo(self, label: str):
        for r in range(self.pages):
            length_row = len(self.photos[r])
            if length_row < self.SLOT_COUNT:
                self.photos[r].append(label)
                return f'{label} photo added successfully on page {r + 1} slot {length_row}'
        return 'No more free slots'

    def display(self):
        result = ''
        for r in range(self.pages):
            length_row = len(self.photos[r])
            result += '-----------\n'
            if length_row > 0:
                result += '[] ' * (length_row - 1) + '[]'
            result += '\n'
        result += '-----------'
        return result
