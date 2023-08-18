main_menu = '''\nГлавное меню
    1: Открыть файл
    2: Сохранить файл
    3: Показать все заметки
    4: Добавить заметку
    5: Найти заметку
    6: Изменить заметку
    7: Удалить заметку
    8: Выход\n'''

input_choice = 'Введите пункт меню: '

load_successful = 'Блокнот успешно открыт!'

load_error = 'Блокнот отстутствует и будет создан при сохранении заметок!'

save_successful = 'Блокнот успешно сохранен!'

notes_empty = 'Список заметок пустой или не загружен!'

new_note = {'HEADER' : 'Введите заголовок: ', 'NOTE' :'Введите заметку: '}

input_new_note = 'Введите данные новой заметки'

def new_note_successful(name: str):
    return f'Заметка {name} успешно добавлена'

input_search = 'Введите значение для поиска: '

def empty_search(word: str) -> str:
    return f'Заметки содержащие значение {word} не найдены!'

input_change = 'Какую заметку мы будем менять: '

change_note = 'Введите новые данные или оставьте поле пустым, чтобы не менять: '

def change_note_successful(name: str):
    return f'Заметка {name} успешно изменена'

input_index = 'Введите номер заметки для изменения: '

input_delete = 'Какую заметку мы будем удалять: '

def delete_note_successful(name: str):
    return f'Заметка {name} успешно удалена'