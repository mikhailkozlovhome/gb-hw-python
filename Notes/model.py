class Notes:

    current_id = 0

    def __init__(self, path: str = 'Notes.csv'):
        self._notes: list[dict[str, str]] = []
        self._path = path

    def open(self):
        try:
            with open(self._path, 'r', encoding = 'UTF8') as file:
                data = file.readlines()
                for note in data:
                    note = note.strip().split(';')
                    new = {'ID' : note[0], 'HEADER' : note[1], 'NOTE' : note[2], 'DATETIME' : note[3]}
                    self.current_id = note[0];
                    self._notes.append(new)
                file.close()
        except FileNotFoundError:
            print("Файл остутствует. Добавьте новую заметку и сохраните файл. Файл создасться автоматически.")

    def get(self):
        return self._notes

    def add(self, new: dict[str, str]) -> str:
        self._notes.append(new)
        return new.get('HEADER')

    def save(self):
        data = []
        for note in self._notes:
            data.append(';'.join([value for value in note.values()]))
        data = '\n'.join(data)
        with open(self._path, 'w', encoding='UTF-8') as file:
            file.write(data)
            file.close()

    def search(self, word: str) -> list[dict[str, str]]:
        result: list[dict[str, str]] = []
        #index = 0
        for note in self._notes:
            #index += 1
            find_note = {}
            for field in note.values():
                if word.lower() in str(field).lower():
                    find_note['ID'] = note.get('ID')
                    find_note['HEADER'] = note.get('HEADER')
                    find_note['NOTE'] = note.get('NOTE')
                    find_note['DATETIME'] = note.get('DATETIME')
                    result.append(find_note)
                    break
        return result

    def change(self, new: dict[str, str], index: int) -> str:
        name = self._notes[index].get('FIO')
        self._notes[index]['FIO'] = new.get('FIO', self._notes[index].get('FIO'))
        self._notes[index]['PHONE'] = new.get('PHONE', self._notes[index].get('PHONE'))
        self._notes[index]['COMMENT'] = new.get('COMMENT', self._notes[index].get('COMMENT'))
        return name

    def delete(self, index: int) -> str:
        return self._notes.pop(index).get('FIO')

            

    
