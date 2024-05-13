from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def area(self):
        return self._width * self._height


class Square(Shape):
    def __init__(self, size):
        self.size = size

    def set_size(self, size):
        self.size = size

    def area(self):
        return self.size ** 2


rect = Rectangle(5, 4)
square = Square(5)

rect.set_width(3)
print(rect.area())
square.set_width(3)
print(square.area())