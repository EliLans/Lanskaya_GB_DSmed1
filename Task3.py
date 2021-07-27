#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    sum = arg1 + arg2 + arg3
    return sum - min(arg1, arg2, arg3)

arg1 = int(input('Введите первое число: '))
arg2 = int(input('Введите второе число: '))
arg3 = int(input('Введите третье число: '))
res = my_func(arg1, arg2, arg3)
print("Сумма наибольших двух чисел: " + str(res))