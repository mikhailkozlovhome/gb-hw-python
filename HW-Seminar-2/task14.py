# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

base = 2
max_number = int(input("Введите верхнюю границу: "))

if max_number > 0:
    power = 1
    while power <= max_number:
        print(f"{power}", end = ' ')
        power *= 2
else:
    print("Верхняя граница должна быть натуральным числом")
