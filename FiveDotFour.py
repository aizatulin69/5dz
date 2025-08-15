def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Give me name and phone please"
        except ValueError:
            return "Give me valid data"
        except KeyError:
            return "No such contact"
    return wrapper


@input_error
def parse_command(command):
    if not command.strip():
        raise ValueError("Empty input")
    parts = command.strip().split()
    action = parts[0].lower()
    args = parts[1:]
    return action, args


def hallo():
    return "Hallo, how can I help you?"


@input_error
def add_contact(args, contacts):
    name, contact = args
    if name in contacts:
        return "Contact already exists."
    contacts[name] = contact
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, new_contact = args
    contacts[name]
    contacts[name] = new_contact
    return "Contact changed."


@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]


def show_all(contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join(
        f"{name}: {number}" for name, number in sorted(contacts.items())
        )


def close():
    return "Good bye!"


@input_error
def main():
    contacts = {}

    while True:
        command = input(">>> ")

        result = parse_command(command)

        if not isinstance(result, tuple):
            print(result)
            continue

        action, args = result

        if action in ("hallo", "hi"):
            print(hallo())
        elif action == "add":
            print(add_contact(args, contacts))
        elif action == "change":
            print(change_contact(args, contacts))
        elif action == "phone":
            print(show_phone(args, contacts))
        elif action == "all":
            print(show_all(contacts))
        elif action in ("close", "exit", "bye"):
            print(close())
            break
        else:
            print("Unknown command. Try again.")


if __name__ == "__main__":
    main()
            

        




