import math


class Shape:
    title = "Фигура"

    def __init__(self):
        self.methods = ["Площадь", "Периметр"]

    def create(self):
        pass

    def input_create(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

    @classmethod
    def title(cls):
        return cls.title

    @staticmethod
    def input_num(message: str):
        while True:
            num = input(message)
            if num.isdigit and float(num) > 0:
                return float(num)
            print("Ошибка! Введите число, > 0: ")


class Square(Shape):
    title = "Квадрат"

    def create(self, a):
        self.a = a

    def input_create(self):
        self.a = self.input_num("Введите сторону: ")

    def area(self):
        return self.a ** 2

    def perimeter(self):
        return self.a * 4


class Rectangle(Square):
    title = "Прямоугольник"

    def create(self, a, b):
        self.a = a
        self.b = b

    def input_create(self):
        self.a = self.input_num("Введите сторону 1: ")
        self.b = self.input_num("Введите сторону 2: ")

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return (self.a + self.b) * 2


class Cube(Square):
    title = "Куб"

    def area(self):
        return 6 * self.a ** 2

    def perimeter(self):
        return self.a * 12


class Parallelepiped(Rectangle):
    title = "Параллелепипед"

    def create(self, a, b, c):
        super().create(a, b)
        self.c = c

    def input_create(self):
        super().input_create()
        self.c = self.input_num("Введите сторону 3: ")

    def area(self):
        return 2 * (self.a * self.b + self.b * self.c + self.a * self.c)

    def perimeter(self):
        return 4 * self.a + 4 * self.b + 4 * self.c


class Circle(Shape):
    title = "Круг"

    def __init__(self):
        super().__init__()
        self.methods.append("Диаметр")

    def create(self, r):
        self.r = r

    def input_create(self):
        self.r = self.input_num("Введите радиус: ")

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r

    def diameter(self):
        return self.r * 2


class Sphere(Circle):
    title = "Сфера"

    def __init__(self):
        self.methods = ["Объём", "Площадь поверхности", "Диаметр"]

    def area(self):
        return (4 / 3) * math.pi * self.r ** 3

    def perimeter(self):
        return 4 * math.pi * self.r ** 2


class Triangle(Shape):
    title = "Треугольник"

    def create(self, a, h):
        self.a = a
        self.h = h

    def input_create(self):
        self.a = self.input_num("Введите сторону: ")
        self.h = self.input_num("Введите высоту: ")

    def area(self):
        return 1 / 2 * self.a * self.h

    def perimeter(self):
        return 2 * math.sqrt(self.a ** 2 - self.h ** 2) + 2 * self.a


class Pyramid(Triangle):
    title = "Пирамида"

    def __init__(self):
        self.methods = ["Объём"]

    def create(self, a, h):
        self.a = a
        self.h = h

    def input_create(self):
        self.a = self.input_num("Введите сторону основания: ")
        self.h = self.input_num("Введите высоту: ")

    def area(self):
        return 1 / 3 * self.a ** 2 * self.h


class Trapezoid(Shape):
    title = "Трапеция"

    def __init__(self):
        self.methods = ["Площадь"]

    def create(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def input_create(self):
        self.a = self.input_num("Введите сторону 1: ")
        self.b = self.input_num("Введите сторону 2: ")
        self.h = self.input_num("Введите высоту: ")

    def area(self):
        return 1 / 2 * self.h * (self.a * self.b)


class Rhombus(Shape):
    title = "Ромб"

    def create(self, d1, d2):
        self.d1 = d1
        self.d2 = d2

    def input_create(self):
        self.d1 = self.input_num("Введите диагональ 1: ")
        self.d2 = self.input_num("Введите диагональ 2: ")

    def area(self):
        return 1 / 2 * self.d1 * self.d2

    def perimeter(self):
        return 2 * math.sqrt(self.d1 ** 2 + self.d2 ** 2)


class Cylinder(Shape):
    title = "Цилиндр"

    def __init__(self):
        self.methods = ["Объём", "Площадь поверхности"]

    def create(self, r, h):
        self.r = r
        self.h = h

    def input_create(self):
        self.r = self.input_num("Введите радиус основания: ")
        self.h = self.input_num("Введите высоту: ")

    def area(self):
        return math.pi * self.r ** 2 * self.h

    def perimeter(self):
        return 2 * math.pi * self.r * (self.h * self.r)


class Cone(Cylinder):
    title = "Конус"

    def area(self):
        return 1 / 3 * self.h * math.pi * self.r ** 2

    def perimeter(self):
        return math.pi * self.r * (self.r + math.sqrt(self.r ** 2
                                                      + self.h ** 2))


def input_menu_item(limit: int) -> int:
    while True:
        num = input("\nВведите номер: ")
        if num.isdigit() and 1 <= int(num) <= limit:
            return int(num) - 1
        print("Ошибка! Попробуйте ещё раз.")


if __name__ == "__main__":
    print("1. Запуск интерфейса \n2. Запуск автотестов")
    num = input_menu_item(2)

    if num == 0:
        shapes = [Circle(), Square(), Rectangle(), Triangle(), Trapezoid(),
                  Rhombus(), Sphere(), Cube(), Parallelepiped(), Pyramid(),
                  Cylinder(), Cone()]

        print("\nВыберите фигуру:")
        for i in range(len(shapes)):
            print(f"{i + 1}. {shapes[i].title}")
        num = input_menu_item(len(shapes))
        shape = shapes[num]
        print(f"\nВы выбрали фигуру {shape.title.lower()}.")
        shape.input_create()
        print(f"Фигура {shape.title.lower()} создана!")

        methods = shape.methods
        print("\nВыберите, что нужно вычислить: ")
        for i in range(len(methods)):
            print(f"{i + 1}. {methods[i]}")
        while True:
            num = input_menu_item(len(methods))
            print(f"{methods[num]}:", end=" ")
            if num == 0:
                print(shape.area())
            elif num == 1:
                print(shape.perimeter())
            elif num == 2 and shape.title in ("Круг", "Сфера"):
                print(shape.diameter())

    else:
        print("Проверка фигуры круг...")
        shape = Circle()
        shape.create(3)
        assert shape.area() == 28.274333882308138
        assert shape.perimeter() == 18.84955592153876
        assert shape.diameter() == 6

        print("Проверка фигуры квадрат...")
        shape = Square()
        shape.create(4)
        assert shape.area() == 16
        assert shape.perimeter() == 16

        print("Проверка фигуры прямоугольник...")
        shape = Rectangle()
        shape.create(2, 4)
        assert shape.area() == 8
        assert shape.perimeter() == 12

        print("Проверка фигуры треугольник...")
        shape = Triangle()
        shape.create(12, 5)
        assert shape.area() == 30
        assert shape.perimeter() == 45.817424229271424

        print("Проверка фигуры трапеция...")
        shape = Trapezoid()
        shape.create(5, 6, 3)
        assert shape.area() == 45

        print("Проверка фигуры ромб...")
        shape = Rhombus()
        shape.create(8, 9)
        assert shape.area() == 36
        assert shape.perimeter() == 24.08318915758459

        print("Проверка фигуры сфера...")
        shape = Sphere()
        shape.create(2)
        assert shape.area() == 33.510321638291124
        assert shape.perimeter() == 50.26548245743669
        assert shape.diameter() == 4

        print("Проверка фигуры куб...")
        shape = Cube()
        shape.create(5)
        assert shape.area() == 150
        assert shape.perimeter() == 60

        print("Проверка фигуры параллелепипед...")
        shape = Parallelepiped()
        shape.create(5, 4, 2)
        assert shape.area() == 76
        assert shape.perimeter() == 44

        print("Проверка фигуры пирамида...")
        shape = Pyramid()
        shape.create(5, 7)
        assert shape.area() == 58.33333333333333

        print("Проверка фигуры цилиндр...")
        shape = Cylinder()
        shape.create(3, 7)
        assert shape.area() == 197.92033717615698
        assert shape.perimeter() == 395.84067435231395

        print("Проверка фигуры конус...")
        shape = Cone()
        shape.create(4, 6)
        assert shape.area() == 100.53096491487338
        assert shape.perimeter() == 140.8828696505485

        print("\nВсе тесты успешно пройдены!")
