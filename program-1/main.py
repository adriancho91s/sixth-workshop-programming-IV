from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self._side = None
        self.side = side  # Setter

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value > 0:
            self._side = value
        else:
            raise ValueError("Side must be a positive number")

    def calculate_area(self):
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self._width = None
        self._height = None
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError("Width must be a positive number")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("Height must be a positive number")

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self._base = None
        self._height = None
        self.base = base
        self.height = height

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        if value > 0:
            self._base = value
        else:
            raise ValueError("Base must be a positive number")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("Height must be a positive number")

    def calculate_area(self):
        return (self.base * self.height) / 2


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self._radius = None
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be a positive number")

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Calculate area of a Square")
        print("2. Calculate area of a Rectangle")
        print("3. Calculate area of a Triangle")
        print("4. Calculate area of a Circle")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            side = float(input("Enter the side of the square: "))
            square = Square(side)
            print(f"Area of the square: {square.calculate_area()}")
        elif choice == '2':
            width = float(input("Enter the width of the rectangle: "))
            height = float(input("Enter the height of the rectangle: "))
            rectangle = Rectangle(width, height)
            print(f"Area of the rectangle: {rectangle.calculate_area()}")
        elif choice == '3':
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            triangle = Triangle(base, height)
            print(f"Area of the triangle: {triangle.calculate_area()}")
        elif choice == '4':
            radius = float(input("Enter the radius of the circle: "))
            circle = Circle(radius)
            print(f"Area of the circle: {circle.calculate_area()}")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
