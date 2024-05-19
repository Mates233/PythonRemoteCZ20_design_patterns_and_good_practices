"""
Vzor Visitor řeší problém mnoha složitých algoritmů, které aplikace používá.
Jeho účelem je oddělit definice algoritmů od objektů, na kterých je lze použít.

Visitor je zřídka používaný vzor kvůli své složitosti.

Design
Abychom mohli použít vzor Visitor, musíme vytvořit:

společné rozhraní představující prvky, na kterých lze provést určitý algoritmus.
Kromě metod specifických pro možné akce by měla existovat metoda pro "přijetí" objektu Visitor
implementace výše uvedených rozhraní
rozhraní reprezentující Visitor, které má schopnost "navštívit" jednotlivé implementace prvků
(obvykle metoda na implementaci), a jeho implementaci.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor):
        visitor.visit_rectangle(self)


class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass


class AreaCalculator(ShapeVisitor):
    def visit_circle(self, circle):
        area = 3.14 * circle.radius * circle.radius
        print(f"Area of circle: {area}")

    def visit_rectangle(self, rectangle):
        area = rectangle.width * rectangle.height
        print(f"Area of rectangle: {area}")


if __name__ == "__main__":
    shapes = [
        Circle(5),
        Rectangle(4, 6)
    ]

    area_calculator = AreaCalculator()

    for shape in shapes:
        shape.accept(area_calculator)

