def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return f"Error: Contact with the name '{name}' does not exist."
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        return f"Error: Contact with the name '{name}' does not exist."
    return f"{contacts[name]}."

def all_contacts(contacts):
    contact_list = "\n".join([f"{name}, {phone}" for name, phone in contacts.items()])
    return contact_list
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(all_contacts(contacts))                  
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
