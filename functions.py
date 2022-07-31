from classes import *
import re

phone_pattern = "\s\+?[-\s]?(?:\d{2,3})?[-\s]?(?:\([-\s]?\d{2,3}[-\s]?\)|\d{2,3})?[-\s]?\d{2,3}[-\s]?\d{2,3}[-\s]?\d{2,3}\s"
no_number = "Sorry, I can't identify a phone number."
no_name = "Sorry, I can't identify a contact's name."


def confirm(question):
    while True:
        string = input(question)
        if string.strip().lower() in ("y", "yes"):
            return True
        if string.strip().lower() in ("n", "no"):
            return False


def find_name_number(text: str):  # return tuple of name and number
    text += " "
    pattern = re.compile(phone_pattern)
    only_name = text
    if not pattern.findall(text):
        return find_name(text), ""
    for x in pattern.findall(text):
        only_name = only_name[:only_name.find(x)]
    return find_name(only_name), str(pattern.findall(text)[0]).strip().replace(" ", "").replace("", ""),


def find_name(text: str):  # converts text into name. Should be used only after the numer has been extracted.
    return text.strip().lower().title()


def add_contact(book: AddressBook, data: str):
    name, number = find_name_number(data)
    if not name:
        return no_name
    elif name in book.data.keys():
        return f"Contact '{name}' already exists"
    else:
        record = Record(Name(name), [Phone(number)] if number else [])
        book.add_record(record)
        return f"Created contact '{name}': '{number}'"


def show_all(book: AddressBook, *_):
    if not book.data:
        return "Your phone book is empty."
    else:
        for name in book.data.keys():
            return f"{name}: {', '.join([x.value for x in book.data.get(name).phones])}"


def phone(book: AddressBook, data: str):
    name = find_name(data)
    if not name:
        return "Sorry, I can't identify a contact's name"
    if name not in book.data.keys():
        return f"Contact '{name}' is not in your contacts"
    else:
        return f"{name}: {', '.join([x.value for x in book.data.get(name).phones])}"


def add_number(book: AddressBook, data: str):
    name, number = find_name_number(data)
    if not name:
        return no_name
    elif not number:
        return no_number
    elif name not in book.data.keys():
        add_contact(book, data)
        return f"Created a new contact '{name}' with number '{number}'"
    else:
        book.data[name].add_number(Phone(number))
        return f"Number '{number}' has been added to contact '{name}'"


def delete_number(book: AddressBook, data: str):
    name, number = find_name_number(data)
    if name and not number:
        if name in book.data.keys():
            if confirm(f"Do you want to delete all numbers from contact '{name}'? Type 'yes'/'no'.\n"):
                book.data[name] = Record(Name(name))
                return f"Done!"
        else:
            return f"Contact {name} does not exist."
    elif name and number:
        if name in book.data.keys():
            if number in [x.value for x in book.data.get(name).phones]:
                book.data.get(name).del_number(Phone(number))
                return f"Number '{number}' has been deleted from contact '{name}'"
            else:
                return f"Contact '{name}' has no phone number '{number}'."
    else:
        return no_name


def delete_contact(book: AddressBook, data: str):
    name, number = find_name_number(data)
    if not name:
        return no_name
    elif name in book.data.keys():
        if confirm(f"Contact '{name}' will be deleted from your phone book. Are you sure? Type 'yes' or 'no'.\n"):
            book.delete_record(name)
            return "Done!"


def help_me(*_):
    return "Hi! Here is the list of known commands:\n" + \
           "\tshow all: shows all your contacts\n" + \
           "\tphone 'name': shows all phone numbers of the contact\n" + \
           "\tadd contact 'name' 'phone number': creates a new contact\n" + \
           "\tdelete contact 'name': deletes contact 'name'\n" + \
           "\tadd phone 'name' 'phone numer': adds the phone number to the existing contact or creates a new one\n" + \
           "\tdelete phone 'name' 'phone number': deletes the phone number from contact\n" + \
           "\texit: close the assistant\n"
