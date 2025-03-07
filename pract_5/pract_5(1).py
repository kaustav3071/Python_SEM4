class Shape:

    @staticmethod
    def describe():
        return "Shapes are geometric objects with area."

    def area(self):
        return 0

class Circle(Shape):
    _pi = 3.14159

    def __init__(self, radius):
        self.__radius = radius

    @classmethod
    def change_pi(cls, new_pi):
        cls._pi = new_pi

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self.__radius = value

    def area(self):
        return self._pi * self.__radius ** 2


class Rectangle(Shape):

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value < 0:
            raise ValueError("Length cannot be negative.")
        self.__length = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width cannot be negative.")
        self.__width = value

    def area(self):
        return self.__length * self.__width


def main():
    print(Shape.describe())

  
    circle = Circle(5)
    print(f"Circle area: {circle.area()}")

    print(f"Original radius: {circle.radius}")
    circle.radius = 10
    print(f"Updated radius: {circle.radius}")
    print(f"Circle area after radius change: {circle.area()}")

    Circle.change_pi(3.14)
    print(f"Circle area with modified pi: {circle.area()}")

    rectangle = Rectangle(4, 6)
    print(f"Rectangle area: {rectangle.area()}")


    rectangle.length = 8
    rectangle.width = 10
    print(f"Updated Rectangle area: {rectangle.area()}")


if __name__ == "__main__":
    main()
