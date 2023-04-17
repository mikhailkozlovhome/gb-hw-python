# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
import random

number_of_coin = int(input("Введите количество монет: "))
i = 1
eagle_coin = 0
tails_coin = 0

while i <= number_of_coin:
# for i in range(1, number + 1):
    coin = random.randint(0,1)
    print(coin, end=" ")
    if coin == 1:
        eagle_coin += 1
    else:
        tails_coin += 1
    i += 1
if eagle_coin <= tails_coin:
    print(f"\nМинимальное количество монет, которые нужно перевернуть равно {eagle_coin}")
else:
    print(f"\n\nМинимальное количество монет, которые нужно перевернуть равно {tails_coin}")