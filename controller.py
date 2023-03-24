import view
import contact

pb = contact.Phonebook('phone.json')

def start():
    while True:
        choice = view.main_menu()

        if choice == str(1):
            pb.open_the_book()
        elif choice == str(2):
            pb.write_in()
        elif choice == str(3):
            pb.searching()
        elif choice == str(4):
            pb.new_contact()
        elif choice == str(5):
            pb.delete_contact()
        elif choice == str(6):
            pb.modifying_contact()
        elif choice == str(7):
            if pb.exit_menu() == 0: break
        else:
            view.wrong_input()
            view.main_menu()