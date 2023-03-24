from colorama import Fore, Style


def main_menu():
    print('\n', f"{'CHOOSE THE ACTION': ^30}", '\n', f"{'MENU BAR': ^30}", '\n', '#' * 33, '\n',
          Fore.GREEN + Style.BRIGHT + 'Press 1 to open the phone book', '\n',
          'Press 2 to save the file', '\n',
          'Press 3 to search the contact information', '\n',
          'Press 4 to add a contact', '\n',
          'Press 5 to delete a contact', '\n',
          'Press 6 to modify a contact data', '\n',
          'Press 7 to exit',
          Style.RESET_ALL + " ")

    choice = input("Enter your choice ")
    return choice


def text_message(init_message):
    match init_message:
        case 'open_the_book':
            return print('The book is opened. What do you want to do next? ')
        case 'changes_is_saved':
            return print('Changes is saved. What do you want to do next? ')
        case 'enter_any_attribute_to_search':
            return print('Enter the contact info you want to search: ')
        case 'info_is_found':
            return print('Info is found. What do you want to do next? ')
        case 'info_is_not_found':
            return print('Info is not found. What do you want to do next? ')
        case 'to_modify':
            contact_to_modify = input("What contact info do you want to modify? ")
            return contact_to_modify
        case 'get_attribute_to_modify':
            attribute = input("What attribute do you want to modify: name, num, info? ")
            return attribute
        case 'new_att_is_name':
            new_attribute_name = input("Enter new name of the contact ")
            return new_attribute_name
        case 'new_att_is_number':
            new_attribute_number = input("Enter new number of the contact ")
            return new_attribute_number
        case 'new_att_is_info':
            new_attribute_info = input("Enter new info of the contact ")
            return new_attribute_info
        case 'leave_the_menu':
            answer = input("Do you want to leave? (y/n) ")
            return answer
        case 'enter_name_number_info':
            new_name = input("Enter the name of the new contact ")
            new_number = input("Enter the number of the new contact ")
            new_info = input("Enter the info about the new contact ")
            return new_name, new_number, new_info
        case 'to_delete':
            contact_to_delete = input("Enter the name of the contact to delete ")
            return contact_to_delete


def print_the_contact_info(book, key):
    print()
    for i in range(len(book[key])):
        print(f'{book[key][i]:^20}', end='')
    print()


def wrong_input():
    return print('Wrong input')