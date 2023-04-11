# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input("Введите трехзначное число: "))
tmp_numb = int(number)
sum_digital = 0

sum_digital = sum_digital + tmp_numb % 10
tmp_numb = int(tmp_numb/10)
sum_digital = sum_digital + tmp_numb % 10
tmp_numb = int(tmp_numb/10)
sum_digital = sum_digital + tmp_numb % 10

print(f"Сумма цифр числа {number} равна {sum_digital}")