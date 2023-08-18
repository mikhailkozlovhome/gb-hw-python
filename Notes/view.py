import text

def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        

def print_message(message: str):
    print('\n' + '='*len(message))
    print(message)
    print('='*len(message) + '\n')

def print_notes(notes: list[dict[str, str]], error: str):
    if notes:
        print('\n' + '='*150)
        for i, note in enumerate(notes, 1):
            print(f'{i:>3}. {note.get("ID"):<10} | {note.get("HEADER"):<20} | {note.get("NOTE"):<80} | {note.get("DATETIME")}')
        print('\n' + '='*150)
    else:
        print_message(error)

def input_note(message) -> dict[str, str]:
    new = {}
    print(message)
    for key, txt in text.new_note.items():
        value = input(txt)
        if value:
            new[key] = value
    return new

def input_search(message) -> str:
    return input(message)