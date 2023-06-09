# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

import random
number_of_elements = int(input("Введите количество кустов на грядке: "))
my_list = [random.randint(1, number_of_elements) for i in range(number_of_elements)]
print(my_list)

# max_numb_of_berries = 0

# for i in range(len(my_list)):
#     if i < len(my_list) - 1:
#         if (my_list[i-1] + my_list[i] + my_list[i+1]) > max_numb_of_berries:
#             max_numb_of_berries = (my_list[i-1] + my_list[i] + my_list[i+1])
#     else:
#         if (my_list[i-1] + my_list[i] + my_list[i+1-len(my_list)]) > max_numb_of_berries:
#             max_numb_of_berries = (my_list[i-1] + my_list[i] + my_list[i+1])
        
# print(f"Максимальное число ягод равно {max_numb_of_berries}")

max_numb_of_berries = 0

for i in range(len(my_list)-1):
    if (my_list[i-1] + my_list[i] + my_list[i+1]) > max_numb_of_berries:
        max_numb_of_berries = (my_list[i-1] + my_list[i] + my_list[i+1])

print(f"Максимальное число ягод равно {max_numb_of_berries}")