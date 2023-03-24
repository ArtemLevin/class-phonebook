import json
import view

path = 'phone.json'

class Phonebook():

    def __init__(self, path: str):
        self.path = path

    def read_out(self):
        with open(self.path, 'r', encoding="UTF-8") as some_file:
            some_content = some_file.read()
            book = json.loads(some_content)
        return book

    def open_the_book(self):
        book = self.read_out()
        for key in book:
            view.print_the_contact_info(book, key)
        return view.text_message('open_the_book')


    def write_in_new_contact(self, book: dict):
        with open(self.path, 'w', encoding="UTF-8") as some_file:
            some_content = json.dumps(book)
            some_file.write(some_content)
        return view.text_message('changes_is_saved')

    def write_in(self):
        book = self.read_out()
        with open(self.path, 'w', encoding="UTF-8") as some_file:
            some_content = json.dumps(book)
            some_file.write(some_content)
        return view.text_message('changes_is_saved')

    def searching(self):
        book = self.read_out()
        view.text_message('enter_any_attribute_to_search')
        data_to_search = input()
        counter = 0
        for key in book:
            if data_to_search in book[key]:
                view.print_the_contact_info(book, key)
                view.text_message('info_is_found')
                counter += 1
        if counter == 0: view.text_message('info_is_not_found')

    def new_contact(self):
        book = self.read_out()
        new_name, new_number, new_info = view.text_message('enter_name_number_info')
        book[new_name] = [new_name] + [new_number] + [new_info]
        self.write_in_new_contact(book)

    def delete_contact(self):
        book = self.read_out()
        contact_to_delete = view.text_message('to_delete')
        if contact_to_delete in book.keys():
            del book[contact_to_delete]
            self.write_in_new_contact(book)

    def modifying_contact(self):
        book = self.read_out()
        contact_to_modify = view.text_message('to_modify')
        if contact_to_modify in book.keys():
            attribute = view.text_message('get_attribute_to_modify')
            if attribute == 'name':
                new_attribute_name = view.text_message('new_att_is_name')
                book[contact_to_modify][0] = new_attribute_name
            elif attribute == 'num':
                new_attribute_num = view.text_message('new_att_is_number')
                book[contact_to_modify][1] = new_attribute_num
            elif attribute == 'info':
                new_info = view.text_message('new_att_is_info')
                book[contact_to_modify][2] = new_info
            self.write_in_new_contact(book)

    def exit_menu(self):
        answer = view.text_message('leave_the_menu')
        if answer == 'y':
            return 0
