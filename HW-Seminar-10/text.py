main_menu = '''\nГлавное меню
    1: Открыть файл
    2: Сохранить файл
    3: Показать все контакты
    4: Добавить контакт
    5: Найти контакт
    6: Изменить контакт
    7: Удалить контакт
    8: Выход\n'''

input_choice = 'Введите пункт меню: '

load_successful = 'Телефонная книга успешно открыта!'

save_successful = 'Телефонная книга успешно сохранена!'

pb_empty = 'Телефонный справочник пустой или не загружен!'

new_contact = {'FIO' : 'Введите ФИО: ', 'PHONE' :'Введите номер телефона: ', 'COMMENT' : 'Введите комментарий: '}

input_new_contact = 'Введите данные нового контакта'

def new_contact_successful(name: str):
    return f'Контакт {name} успешно добавлен'

input_search = 'Введите значение для поиска: '

def empty_search(word: str) -> str:
    return f'Контакты содержащие значение {word} не найдены!'

input_change = 'Какой контакт мы будем менять: '

change_contact = 'Введите новые данные или оставьте поле пустым, чтобы не менять: '

def change_contact_successful(name: str):
    return f'Контакт {name} успешно изменен'

input_index = 'Введите номер контакта для изменения: '

input_delete = 'Какой контакт мы будем удалять: '

def delete_contact_successful(name: str):
    return f'Контакт {name} успешно удален'