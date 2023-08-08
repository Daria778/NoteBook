import datetime

def user_input():
    print("Hello, what can i help you?")
    ask = int(input("Chose an option:\n 1 - add and save\n" 
                    " 2 - edit\n" 
                    " 3 - read \n"
                    " 4 - delete\n" 
                    " 5 - exit\n "))
    return ask
    
def add (notes):
    id = len(notes) + 1
    title = str(input("Enter the title of your note: "))
    body = str(input("Enter the body of your note: "))
    time = datetime.datetime.now().strftime('%Y-%m-%d')
    newNote = {"id": id, "title": title, "body": body, "time": time}
    notes.append(newNote)
    return notes

def edit():
    request = int(input("Enter the id of the note you want to edit: "))
    return request


def delete():
    request = int(input("Enter the id of the note you want to delete: "))
    return request

def exit():
    print("Goodbye!")              