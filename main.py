def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command, try again"
    return inner

contacts = {}

@input_error
def hello():
    return "How can I help you?"

@input_error
def add_contact(command):
    _, name, number = command.split()
    contacts[name] = number
    return f"Contact {name} with number {number} has been added"

@input_error
def change_contact(command):
    _, name, number = command.split()
    contacts[name] = number
    return f"Number for {name} has been changed to {number}"

@input_error
def get_phone(command):
    _, name = command.split()
    return f"The phone number for {name} is {contacts[name]}"

@input_error
def show_all():
    return "\n".join([f"{name}: {number}" for name, number in contacts.items()])

def main():
    while True:
        user_input = input("Enter command: ").lower().strip()
        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif user_input == "hello":
            print(hello())
        elif user_input.startswith("add"):
            print(add_contact(user_input))
        elif user_input.startswith("change"):
            print(change_contact(user_input))
        elif user_input.startswith("phone"):
            print(get_phone(user_input))
        elif user_input == "show all":
            print(show_all())
        else:
            print("Invalid command, try again")

if __name__ == "__main__":
    main()
