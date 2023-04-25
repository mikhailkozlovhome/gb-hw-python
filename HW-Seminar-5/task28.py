# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def sum(first_num, second_num):
    if second_num == 0:
        return 0
    return first_num + sum(first_num, second_num - 1)


first_number = int(input("Введите 1-е число: "))
second_number = int(input("Введите 2-е число: "))

print(f"Сумма чисел {first_number} и {second_number} равна {sum(first_number, second_number)}")