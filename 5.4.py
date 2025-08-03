all_contacts = []

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return print("Enter name and phone please")
        except ValueError:
            return print("Phone must be digit")
        except KeyError:
            return print("No such contact")
    return wrapper

def main(comand):
    @input_error
    def hallo():
        print('Hallo, how can I help you?')

    @input_error
    def add_contact(comand_input):
        text = comand_input.strip().split(' ')
        name = text[1]
        contact = text[2]
        if not contact.isdigit():
            raise ValueError
        all_contacts.append({name: contact})
        print('Contact added.')

    @input_error
    def change_contact(comand_input):
        text = comand_input.strip().split(' ')
        name = text[1]
        new_contact = text[2]
        for i in range(len(all_contacts)):
            if name in all_contacts[i]:
                all_contacts[i][name] = new_contact
                print("Contact changed.")
                return
        raise KeyError

    @input_error
    def show_phone(comand_input):
        text = comand_input.strip().split(' ')
        name = text[1]
        for contact in all_contacts:
            if name in contact:
                print(contact[name])
                return
        raise KeyError

    def show_all():
        print(all_contacts)

    def close():
        print("Good bye!")

    action = comand.strip().split(' ')[0]

    if action.lower() in ('hallo', 'hi'):
        hallo()
    elif action.lower() == 'add':
        add_contact(comand)
    elif action.lower() == 'change':
        change_contact(comand)
    elif action.lower() == 'phone':
        show_phone(comand)
    elif action.lower() == 'all':
        show_all()
    elif action.lower() in ('close', 'exit'):
        close()
        return False
    else:
        print('Please, enter another command')
    return True

while True:
    command = input(">>> ")
    if not main(command):
        break
            
        