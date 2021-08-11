#3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.

class OwnError (Exception):

    def func_str(self, my_list):
        try:
            for el in my_list:
                if type(el) == str:
                    raise OwnError("в списке присутствует элемент типа данных строка: ")

        except OwnError as err:
            print(err, el)


    def func_bool(self, my_list):
        try:
            for el in my_list:
                if type(el) == bool:
                    raise OwnError("в списке присутствует элемент типа данных строка: ")
        except OwnError as err:
            print(err, el)


input_list = [2, 1.2, 'блаблабла', True]
print("Исходный список: ", input_list, "\n")
my_err = OwnError()
my_err.func_str(input_list)
my_err.func_bool(input_list)