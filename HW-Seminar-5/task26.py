# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

def power(base, pow):
    if pow == 1:
        return base
    return base * power(base, pow - 1)


base_number = int(input("Введите число: "))
power_number = int(input("Введите степень в которую надо возвести число: "))

print(f"Число {base_number} в степени {power_number} равно {power(base_number, power_number)}")