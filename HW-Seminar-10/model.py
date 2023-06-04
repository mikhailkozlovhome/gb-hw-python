class PhoneBook:
    def __init__(self, path: str = 'phonebook.txt'):
        self._phone_book: list[dict[str, str]] = []
        self._path = path

    def open(self):
        with open(self._path, 'r', encoding = 'UTF8') as file:
            data = file.readlines()
            for contact in data:
                contact = contact.strip().split(';')
                new = {'FIO' : contact[0], 'PHONE' : contact[1], 'COMMENT' : contact[2]}
                self._phone_book.append(new)
            file.close()

    def get(self):
        return self._phone_book

    def add(self, new: dict[str, str]) -> str:
        self._phone_book.append(new)
        return new.get('FIO')

    def save(self):
        data = []
        for contact in self._phone_book:
            data.append(';'.join([value for value in contact.values()]))
        data = '\n'.join(data)
        with open(self._path, 'w', encoding='UTF-8') as file:
            file.write(data)
            file.close()

    def search(self, word: str) -> list[dict[str, str]]:
        result: list[dict[str, str]] = []
        index = 0
        for contact in self._phone_book:
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

    def change(self, new: dict[str, str], index: int) -> str:
        name = self._phone_book[index].get('FIO')
        self._phone_book[index]['FIO'] = new.get('FIO', self._phone_book[index].get('FIO'))
        self._phone_book[index]['PHONE'] = new.get('PHONE', self._phone_book[index].get('PHONE'))
        self._phone_book[index]['COMMENT'] = new.get('COMMENT', self._phone_book[index].get('COMMENT'))
        return name

    def delete(self, index: int) -> str:
        return self._phone_book.pop(index).get('FIO')

            

    
