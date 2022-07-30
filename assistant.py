import classes
from commands import commands, def_mod


def main():
    print("Welcome to your personal Python assistant!")
    print("What can I do for you today?")
    book = classes.AddressBook()
    while True:
        command = input()
        mode, data = def_mod(command)
        commands.get(mode)(book, data)


if __name__ == "__main__":
    main()
