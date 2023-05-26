# Открывать файл
# Файл в режим txt
# Сохранить файл
# Показать все контакты
# Добавить контакт
# Найти контакт
# Удалить контакт
# Выход

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

#Поля ФИО телефон комментарий

import os

def menu(header = "Введите пункт меню:") -> int:
    print(header)
    print("1: Открыть файл")
    print("2: Сохранить файл")
    print("3: Показать все контакты")
    print("4: Добавить контакт")
    print("5: Найти контакт")
    print("6: Удалить контакт")
    print("7: Выход")
    result = int(input())
    os.system('clear')
    return result

os.system('clear')
selector = menu()
while selector != 7:
    if selector == 1:
        selector = menu()
    elif selector == 2:
        selector = menu()
    elif selector == 3:
        selector = menu()   
    elif selector == 4:
        selector = menu() 
    elif selector == 5:
        selector = menu()    
    elif selector == 6:
        selector = menu()    
    else:
        selector = menu("Такого пункта меню нет, введите снова:")