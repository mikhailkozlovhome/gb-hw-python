import model
import view
import text

def start():
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                model.open_pb()
                view.print_message(text.load_successful)
            case 2:
                pass
            case 3:
                pb = model.get_pb()
                view.print_contacts(pb, text.pb_empty)
            case 4:
                contact = view.input_contact()
                name = model.add_contact(contact)
                view.print_message(text.new_contact_successful(name))
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                break