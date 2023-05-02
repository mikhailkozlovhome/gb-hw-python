# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

first_element = int(input("Введите первый элемент прогрессии: "))
progression_difference = int(input("Введите разность прогрессии: "))
number_of_elements = int(input("Введите количество элементов прогрессии: "))

print(my_list := [first_element + (i - 1) * progression_difference for i in range(1, number_of_elements + 1)])