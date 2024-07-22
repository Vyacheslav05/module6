import math

class Figure:
    def __init__(self, color, sides, filled=True):
        self.sides_count = 0
        self.__color = color
        self.__sides = sides
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    def __init__(self, color, side, filled=True):
        super().__init__(color, [side], filled)
        self.sides_count = 1
        self.__radius = side / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2

class Triangle(Figure):
    def __init__(self, color, sides, filled=True):
        super().__init__(color, sides, filled)
        self.sides_count = 3
        self.__height = self.__calculate_height()

    def __calculate_height(self):
        a, b, c = self.__sides
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return (2 * area) / a

    def get_square(self):
        return 0.5 * self.__sides[0] * self.__height

class Cube(Figure):
    def __init__(self, color, side, filled=True):
        super().__init__(color, [side] * 12, filled)
        self.sides_count = 12
        self.__sides = [side] * 12

    def set_sides(self, *new_sides):
        if len(new_sides) == 1 and self.__is_valid_sides(new_sides[0]):
            self.__sides = [new_sides[0]] * 12

    def get_volume(self):
        return self.__sides[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)
print(circle1.get_color())  # Изменится
cube1.set_color(300, 70, 15)
print(cube1.get_color())  # Не изменится

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())  # Не изменится
circle1.set_sides(15)
print(circle1.get_sides())  # Изменится

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())