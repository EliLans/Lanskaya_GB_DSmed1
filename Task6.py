#6. Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import cycle, count

n = 100
num_list = [x for x in range(3)]
counter = count()
cycler = cycle(num_list)

print([next(counter) for x in range(n)])
print([next(cycler) for x in range(n)])