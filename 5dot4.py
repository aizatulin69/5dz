
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return print("Give me name and phone please")
        except ValueError:
            return print("Give me valid data")
        except KeyError:
            return print("No such contact")
    return wrapper


@input_error
def parse_command(command):
    parts = command.strip().split()
    action = parts[0].lower()
    args = parts[1:]
    return action, args


@input_error
def hello():
    return 'Hello, how can I help you?'


@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        return "Please enter name and phone number."
    name, contact = args[0], args[1]
    if not contact.isdigit():
        return "Invalid phone number."
    if name in contacts:
        return "Contact already exists."
    contacts[name] = contact
    return "Contact added."


@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        return "Please enter name and new phone number."
    name, new_contact = args[0], args[1]
    if name in contacts:
        contacts[name] = new_contact
        return "Contact changed."
    return "Contact not found."


@input_error
def show_phone(args, contacts):
    if len(args) < 1:
        return "Please enter name."
    name = args[0]
    return contacts.get(name, "Contact not found.")


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts available."
    return '\n'.join(f"{name}: {number}" for name, number in sorted(contacts.items()))


@input_error
def close():
    return "Good bye!"


@input_error
def main():
    contacts = {}

    while True:
        command = input(">>> ")
        action, args = parse_command(command)

        if action in ('hello', 'hi'):
            print(hello())
        elif action == 'add':
            print(add_contact(args, contacts))
        elif action == 'change':
            print(change_contact(args, contacts))
        elif action == 'phone':
            print(show_phone(args, contacts))
        elif action == 'all':
            print(show_all(contacts))
        elif action in ('close', 'exit', 'bye'):
            print(close())
            break
        else:
            print("Unknown command. Try again.")


if __name__ == "__main__":
    main()
            

        

