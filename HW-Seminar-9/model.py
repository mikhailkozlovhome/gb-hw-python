phone_book: list[dict[str, str]] = []
path = 'phonebook.txt'

def open_pb():
    global phone_book
    with open(path, 'r', encoding = 'UTF8') as file:
        data = file.readlines()
        for contact in data:
            contact = contact.strip().split(';')
            new = {'FIO' : contact[0], 'PHONE' : contact[1], 'COMMENT' : contact[2]}
            phone_book.append(new)
        file.close()

def get_pb():
    global phone_book
    return phone_book

def add_contact(new: dict[str, str]) -> str:
    global phone_book
    phone_book.append(new)
    return new.get('FIO')

def save_pb():
    global phone_book
    data = []
    for contact in phone_book:
        data.append(';'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)
        file.close()

def search_contact(word: str) -> list[dict[str, str]]:
    global phone_book
    result: list[dict[str, str]] = []
    index = 0
    for contact in phone_book:
        index += 1
        find_contact = {}
        for field in contact.values():
            if word.lower() in field.lower():
                find_contact['FIO'] = contact.get('FIO')
                find_contact['PHONE'] = contact.get('PHONE')
                find_contact['COMMENT'] = contact.get('COMMENT')
                find_contact['INDEX'] = index - 1
                result.append(find_contact)
                break
    return result

def change_contact(new: dict[str, str], index: int) -> str:
    global phone_book
    name = phone_book[index].get('FIO')
    phone_book[index]['FIO'] = new.get('FIO', phone_book[index].get('FIO'))
    phone_book[index]['PHONE'] = new.get('PHONE', phone_book[index].get('PHONE'))
    phone_book[index]['COMMENT'] = new.get('COMMENT', phone_book[index].get('COMMENT'))
    return name

def delete_contact(index: int) -> str:
    global phone_book
    return phone_book.pop(index).get('FIO')

            

    
