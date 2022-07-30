import sys
from functions import add_contact, show_all, phone, add_number, help_me, delete_number, delete_contact

commands = {
    "exit": lambda *_: sys.exit(),
    "hello": lambda *_: print("How can I help you?"),
    "bye": lambda *_: (print("Good bye!"), sys.exit()),
    "add_contact": add_contact,
    "add_number": add_number,
    "delete_contact": delete_contact,
    "delete_number": delete_number,
    "phone": phone,
    "show_all": show_all,
    "help_me": help_me,
    "empty": lambda *_: print("Use 'help' command to know what I can."),
    0: lambda *_: print("Sorry I can't understand you. Try 'help' command to see what I can."),
}


def def_mod(string: str):
    try:
        mods = {
            ".": "exit",
            "hello": "hello",
            "good bye": "bye",
            "close": "bye",
            "exit": "bye",
            "add contact": "add_contact",
            "add phone": "add_number",
            "add number": "add_number",
            "add": "add_contact",
            "delete contact": "delete_contact",
            "delete phone number": "delete_number",
            "delete phone": "delete_number",
            "delete number": "delete_number",
            "phone": "phone",
            "show all": "show_all",
            "help": "help_me",
        }
        if not string:
            return "empty", ""
        for key_word in mods.keys():
            if key_word in string.lower():
                return mods[key_word], string.replace(key_word, "")
        return 0, ""
    except Exception as err:
        return err
