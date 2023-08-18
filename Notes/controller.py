import model
import view
import text

my_notes = model.Notes()

def start():
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                my_notes.open()
                view.print_message(text.load_successful)
            case 2:
                my_notes.save()
                view.print_message(text.save_successful)
            case 3:
                notes = my_notes.get()
                view.print_notes(notes, text.notes_empty)
            case 4:
                note = view.input_note(text.input_new_note)
                my_notes.current_id += 1
                note['ID'] = my_notes.current_id
                from datetime import datetime
                note['DATETIME'] = datetime.now()
                name = my_notes.add(note)
                view.print_message(text.new_note_successful(name))
            case 5:
                key_word = view.input_search(text.input_search)
                result = my_notes.search(key_word)
                view.print_notes(result, text.empty_search(key_word))
            case 6:
                key_word = view.input_search(text.input_change)
                result = my_notes.search(key_word)
                view.print_notes(result, text.empty_search(key_word))

                if result:
                    if len(result) != 1:
                        index = result[int(view.input_search(text.input_index)) - 1].get('INDEX')
                    else:
                        index = result[len(result) - 1].get('INDEX')
                    new_note = view.input_note(text.change_note)
                    name = my_notes.change(new_note, index)
                    view.print_message(text.change_note_successful(name))
            case 7:
                key_word = view.input_search(text.input_delete)
                result = my_notes.search(key_word)
                view.print_notes(result, text.empty_search(key_word))

                if result:
                    if len(result) != 1:
                        index = result[int(view.input_search(text.input_index)) - 1].get('INDEX')
                    else:
                        index = result[len(result) - 1].get('INDEX')
                    name = my_notes.delete(index)
                    view.print_message(text.delete_note_successful(name))
            case 8:
                break