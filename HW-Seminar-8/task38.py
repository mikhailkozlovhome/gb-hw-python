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

def item_2_dict(item):
    item = item.replace("\n", "").split(';')
    item = {"FIO" : item[0], "PHONE" : item[1], "COMMENT" : item[2]}
    return item

def open_and_read_file(path) -> list:
    with open(path, encoding='utf-8') as file:
        data = list(file)
        file.close()
    if len(data) != 0:
       return list(map(item_2_dict, data))        
    return data

def save_file(data, path):
    with open(path, "w", encoding='utf-8') as file:
        for item in data:
            file.write(item.get('FIO') + ';' + item.get('PHONE') + ';' + item.get('COMMENT') + '\n')
        #map(lambda x: file.write(x.get('FIO') + ';' + x.get('PHONE') + ';' + x.get('COMMENT') + '\n'), data)
    file.close()

def show_all_contacts(data):
    index = 0
    for item in data:
        index += 1
        print(f"{index}     {item.get('FIO')}   {item.get('PHONE')}     {item.get('COMMENT')}")

def delete_contact(data):
    index = int(input("Введите номер контакта для удаления: "))
    if index > 0 and index <= len(data):   
        del data[index - 1]
        os.system('clear')
    else:
        print("Введен неверный номер!")
    
def add_contact(data):
    item = dict()
    item["FIO"] = input("Введите фамилию, имя, отчество через пробел: ")
    item["PHONE"] = input("Введите телефон: ")
    item["COMMENT"] = input("Введите комментарий: ")
    data.append(item)
    
def find_contact(data):
    find_str = input("Введите значение для поиска: ")
    for item in data:
        if (str(item.get('FIO')).upper().find(find_str.upper()) > -1
            or str(item.get('PHONE')).upper().find(find_str.upper()) > -1
            or str(item.get('COMMENT')).upper().find(find_str.upper()) > -1):
                print(f"ФИО:    {item.get('FIO')}")
                print(f"Телефон:    {item.get('PHONE')}")
                print(f"Комментарий:    {item.get('COMMENT')}")
                print()

os.system('clear')
selector = menu()
path = "phonebook.txt"
main_list = list()

while selector != 7:
    if selector == 1:
        main_list = open_and_read_file(path)
        selector = menu()
    elif selector == 2:
        save_file(main_list, path)
        selector = menu()
    elif selector == 3:
        show_all_contacts(main_list)
        selector = menu()   
    elif selector == 4:
        add_contact(main_list)
        os.system('clear')
        selector = menu() 
    elif selector == 5:
        find_contact(main_list)
        selector = menu()    
    elif selector == 6:
        show_all_contacts(main_list)
        delete_contact(main_list)
        selector = menu()    
    else:
        selector = menu("Такого пункта меню нет, введите снова:")