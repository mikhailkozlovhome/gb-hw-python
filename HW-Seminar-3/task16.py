# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

import random
number_of_elements = int(input("Введите количество элементов: "))
number = int(input("Введите число, которое требуется найти: "))
delta = 5
count = 0

my_list = [random.randint(0, number + delta) for i in range(number_of_elements)]

for item in my_list:
    if item == number:
        count += 1
        
print(my_list)
print(f"Число {number} встречается {count} раз в массиве")