import sys

# Словник для зберігання контактів
contacts = {}

# Функція обробник для команди "hello"
def hello():
    print("How can I help you?")

# Функція обробник для команди "add"
def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} with phone number {phone} has been added")

# Функція обробник для команди "change"
def change_phone(name, phone):
    if name in contacts:
        contacts[name] = phone
        print(f"Phone number for {name} has been changed to {phone}")
    else:
        print(f"{name} is not in contacts")

# Функція обробник для команди "phone"
def show_phone(name):
    if name in contacts:
        print(f"The phone number for {name} is {contacts[name]}")
    else:
        print(f"{name} is not in contacts")

# Функція обробник для команди "show all"
def show_all():
    if not contacts:
        print("There are no contacts")
    else:
        print("Contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

# Декоратор для перехоплення помилок
def handle_errors(func):
    def wrapper(*args):
        try:
            func(*args)
        except Exception as e:
            print(f"Error: {e}")
    return wrapper

# Функція парсера команд
def parse_command(command):
    tokens = command.strip().split()
    if not tokens:
        return None, None
    if tokens[0].lower() == "hello":
        return hello, None
    if tokens[0].lower() == "add" and len(tokens) == 3:
        return add_contact, (tokens[1], tokens[2])
    if tokens[0].lower() == "change" and len(tokens) == 3:
        return change_phone, (tokens[1], tokens[2])
    if tokens[0].lower() == "phone" and len(tokens) == 2:
        return show_phone, (tokens[1],)
    if tokens[0].lower() == "show" and tokens[1].lower() == "all":
        return show_all, None
    return None, None

# Основна функція бота
@handle_errors
def main():
    while True:
        command = input("> ")
        if command.lower() == "exit":
            sys.exit()
        func, args = parse_command(command)
        if func:
            func(*args)
        else:
            print("Unknown command")

if __name__ == '__main__':
    main()
