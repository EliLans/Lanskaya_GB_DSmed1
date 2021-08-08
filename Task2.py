#2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте
# относятся пальто и костюм.

class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_coat_square(self):
        return self.width / 6.5 + 0.5

    def get_jacket_square(self):
        return self.height * 2 + 0.3

    @property
    def get_full_square(self):
        return str(f'Общая площадь ткани: '
                   f' {(self.get_coat_square()) + (self.get_jacket_square())}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.get_coat_square())

    def __str__(self):
        return f'Площадь ткани, требуемая для пальто: {self.square_c}'


class Jacket(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.get_jacket_square())

    def __str__(self):
        return f'Площадь ткани, требуемая на костюм: {self.square_j}'

coat = Coat(5, 10)
jacket = Jacket(3, 5)
print(coat)
print(jacket)
print(coat.get_full_square)
print(jacket.get_full_square)
