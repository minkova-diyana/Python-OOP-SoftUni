class ImageArea:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()


image_1 = ImageArea(5, 2)
image_2 = ImageArea(3, 2)
image_3 = ImageArea(5, 2)
print(image_1 > image_2)
print(image_1 >= image_2)
print(image_2 < image_1)
print(image_2 <= image_1)
print(image_3 == image_1)
print(image_1 != image_2)