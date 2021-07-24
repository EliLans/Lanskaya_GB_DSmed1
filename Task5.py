#Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
#У пользователя нужно запрашивать новый элемент рейтинга.
#Если в рейтинге существуют элементы с одинаковыми значениями,
#то новый элемент с тем же значением должен разместиться после них.

my_list = [8, 7, 5, 4, 3, 3, 2, 2]
number = int(input("Введите число: "))

c = my_list.count(number)
for element in my_list:
    if c > 0:
        i = my_list.index(number)
        my_list.insert(i+c, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print('Обновленный рейтинг: ' + str(my_list))