#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

n = int(input('Введите целое положительное число n: '))
ost = n % 10
b = n // 10
while b > 0:
    if b % 10 > ost:
        ost = b % 10
        if ost == 9:
            break
    b = b // 10
print('Самая большая цифра в числе: ' + str(ost))
