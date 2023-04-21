# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
number_of_elements = int(input("Введите количество элементов: "))
number = int(input("Введите число, с которым необходимо сравнить: "))

shift = 5

my_list = [random.randint(-(abs(number)+shift), abs(number) + shift) for i in range(number_of_elements)]

index = 0

for i in range(len(my_list)):
    if abs(number - my_list[i]) < abs(number - my_list[index]):
        index = i
               
print(my_list)
print(f"Самый близкий по величине элемент массива к числу {number} равен {my_list[index]}")