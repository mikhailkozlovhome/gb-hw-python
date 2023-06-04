import model
import view
import text

my_pb = model.PhoneBook()

def start():
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                my_pb.open()
                view.print_message(text.load_successful)
            case 2:
                my_pb.save()
                view.print_message(text.save_successful)
            case 3:
                pb = my_pb.get()
                view.print_contacts(pb, text.pb_empty)
            case 4:
                contact = view.input_contact(text.input_new_contact)
                name = my_pb.add(contact)
                view.print_message(text.new_contact_successful(name))
            case 5:
                key_word = view.input_search(text.input_search)
                result = my_pb.search(key_word)
                view.print_contacts(result, text.empty_search(key_word))
            case 6:
                key_word = view.input_search(text.input_change)
                result = my_pb.search(key_word)
                view.print_contacts(result, text.empty_search(key_word))

                if result:
                    if len(result) != 1:
                        index = result[int(view.input_search(text.input_index)) - 1].get('INDEX')
                    else:
                        index = result[len(result) - 1].get('INDEX')
                    new_contact = view.input_contact(text.change_contact)
                    name = my_pb.change(new_contact, index)
                    view.print_message(text.change_contact_successful(name))
            case 7:
                key_word = view.input_search(text.input_delete)
                result = my_pb.search(key_word)
                view.print_contacts(result, text.empty_search(key_word))

                if result:
                    if len(result) != 1:
                        index = result[int(view.input_search(text.input_index)) - 1].get('INDEX')
                    else:
                            index = result[len(result) - 1].get('INDEX')
                    name = my_pb.delete(index)
                    view.print_message(text.delete_contact_successful(name))
            case 8:
                break