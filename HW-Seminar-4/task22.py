# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random
number_of_elements_1 = int(input("Введите количество элементов 1-го набора чисел: "))
number_of_elements_2 = int(input("Введите количество элементов 2-го набора чисел: "))

my_list_1 = [random.randint(-number_of_elements_1, number_of_elements_1) for i in range(number_of_elements_1)]
my_list_2 = [random.randint(-number_of_elements_2, number_of_elements_2) for i in range(number_of_elements_2)]

print(f"1-й набор чисел: {my_list_1}")
print(f"2-й набор чисел: {my_list_2}")

result_list = list(set(my_list_1).intersection(set(my_list_2)))
result_list.sort()
print(f"Результат {result_list}")
