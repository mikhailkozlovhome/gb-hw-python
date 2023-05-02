# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

number_of_elements = int(input("Введите количество элементов: "))
min_lim = int(input("Введите минимальное значение диапазона: "))
max_lim = int(input("Введите максимальное значение диапазона: "))

shift = 100


print(my_list := [random.randint(-number_of_elements - shift, number_of_elements + shift) for _ in range(number_of_elements)])

print(res_list := [item for item in my_list if item >= min_lim and item <= max_lim])