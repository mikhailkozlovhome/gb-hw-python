# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите количество долек по ширине: "))
m = int(input("Введите количество долек по длине: "))
k = int(input("Введите количество долек, которые хотите отломить: "))

if k % n == 0 or k % m == 0:
    print(f"от шоколадки размером {n} × {m} долек можно отломить {k} долек за один разлом")
else:
    print(f"от шоколадки размером {n} × {m} долек нельзя отломить {k} долек за один разлом")