#1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

out_f = open("new_file.txt", "w")
str_list = input("Введите ваш текст: \n")

while str_list:
    out_f.write(f'{str_list}\n')
    str_list = input("Введите ваш текст: \n")

out_f.writelines(str_list)
out_f.close()