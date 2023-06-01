phone_book = []
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
            

    
