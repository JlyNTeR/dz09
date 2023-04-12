contacts = {}

while True:
    command = input("What can I do for you? ").lower()

    if command == "hello":
        print("How can I help you?")

    elif command.startswith("add "):
        name, phone = command.split()[1:]
        contacts[name] = phone
        print(f"Added {name} with phone number {phone}")

    elif command.startswith("change "):
        name, phone = command.split()[1:]
        if name in contacts:
            contacts[name] = phone
            print(f"Changed phone number for {name} to {phone}")
        else:
            print(f"{name} not found")

    elif command.startswith("phone "):
        name = command.split()[1]
        if name in contacts:
            print(f"{name}'s phone number is {contacts[name]}")
        else:
            print(f"{name} not found")

    elif command == "show all":
        if contacts:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found")

    elif command in ("good bye", "close", "exit"):
        print("Good bye!")
        break

    else:
        print("Unknown command")
