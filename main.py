contacts = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Invalid key entered. Please try again."
        except ValueError:
            return "Invalid value entered. Please try again."
        except IndexError:
            return "Invalid index entered. Please try again."
    return inner

@input_error
def hello(*args):
    return "How can I help you?"

@input_error
def add(*args):
    list_of_param = args[0].split()
    name = list_of_param[0]
    phone_numbers = list_of_param[1:]
    contacts[name] = phone_numbers
    if not phone_numbers:
        raise IndexError()
    
    return f"Contact {name} added  {phone_numbers} successfully."

@input_error
def change(*args):
    name, phone_number = args.split()
    if name in contacts:
        contacts[name] = [phone_number]
        return "Phone number updated successfully."
    else:
        return "Contact not found."

@input_error
def phone(*args):
    if args in contacts:
        return f"Phone number for {args} is {contacts[args]}"
    else:
        return "Contact not found."

@input_error
def show_all(*args):
    if contacts:
        result = ""
        for name, phone_numbers in contacts.items():
            result += f"{name}: {phone_numbers}\n"
        return result.strip()
    else:
        return "No contacts found."

def exit(*args):
    return "Good bye!"

def no_command(*args):
    return "Unknown command, try again"

COMMANDS = {hello: 'hello',
            add: 'add',
            change: 'change',
            phone: 'phone',
            show_all: 'show all',
            exit: 'exit'}

def command_handler(text):
    for command, kword in COMMANDS.items():
        if text.startswith(kword):
            return command, text.replace(kword, '').strip()
    return no_command, None

def main():
    while True:
        user_input = input("Enter a command: ").lower()
        command, data = command_handler(user_input)
        print(command(data))
        if command == exit:
            break

if __name__ == '__main__':
    main()
