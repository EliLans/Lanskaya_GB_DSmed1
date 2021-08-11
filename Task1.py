#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неправильно введен год'
            else:
                return f'Неправильно введен месяц'
        else:
            return f'Неправильно введен день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('11 - 8 - 2021')
print(today)
print(Data.valid(11, 11, 2032))
print(today.valid(11, 13, 2011))
print(Data.extract('11 - 11 - 2020'))
print(today.extract('11 - 11 - 2022'))
print(Data.valid(1, 1, 2000))