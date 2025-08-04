all_contacts = []

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
def hallo():
    print('Hallo, how can I help you?')

@input_error
def add_contact(comand_input):
    is_repeat = False
    text = comand_input.strip().split(' ')
    name = text[1]
    contact = text[2]
    if not contact.isdigit():
        raise ValueError
    for contact_dict in all_contacts:
        if name in contact_dict:
            is_repeat = True
            break
    if not is_repeat:
        all_contacts.append({name: contact})
        print('Contact added.')
    else:
        print('Contact already exists.')

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


def main():

    while True:
        comand = input(">>> ").strip().lower()

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
        elif action.lower() in ('close', 'exit', 'bye'):
            close()
            return False
        else:
            print('Please, enter another command')

if __name__ == "__main__":
    main()
            

        
