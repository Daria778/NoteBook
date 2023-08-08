import datetime

def user_input():
    print("Hello, what can i help you?")
    ask = int(input("Chose an option:\n 1 - add and save\n" 
                    " 2 - edit\n" 
                    " 3 - read \n"
                    " 4 - read a note\n"
                    " 5 - read notes for the selected date\n"
                    " 6 - delete\n" 
                    " 7 - exit\n "))
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

def readNote():
    request = int(input("Enter the id of the note you want to read: "))
    return request

def time():
    request = input("Enter the date Year-month-day: ")
    time = datetime.datetime.strptime(request, '%Y-%m-%d').date()
    return time

def delete():
    request = int(input("Enter the id of the note you want to delete: "))
    return request

def exit():
    print("Goodbye!")              