def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.lower(), args

def add_contact(username, phone, contacts):
    contacts[username] = phone
    return "Contact added."

def change_contact(username, phone, contacts):
    if username in contacts:
        contacts[username] = phone
        return f"Phone for {username} changed."
    else:
        return f"User {username} not found."

def get_phone(username, contacts):
    return contacts.get(username, f"No phone for {username} found.")

def show_all_contacts(contacts):
    return '\n'.join([f"{username}: {phone}" for username, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        elif command == "add" and len(args) == 2:
            print(add_contact(args[0], args[1], contacts))
        elif command == "change" and len(args) == 2:
            print(change_contact(args[0], args[1], contacts))
        elif command == "phone" and len(args) == 1:
            print(get_phone(args[0], contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        elif command in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
