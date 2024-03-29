import datetime

def delete(data, id):
        for note in data:
            if note["id"] == id:
                data.remove(note)
                print("The note has been deleted")
            break
        return data

def edit(data, id):
     for note in data:
          if note["id"] == id:
                title = str(input("Enter the title of your note: "))
                body = str(input("Enter the body of your note: "))
                note["title"] = title
                note["body"] = body
                note["time"] = datetime.datetime.now().strftime('%Y-%m-%d')
                break
     return data
          
def sort(data):
    data.sort(key = lambda x: x["time"])
    return data

def printNotes(data):
     if not data:
          print("There are no notes")
     else:
          for note in data:
               print(f'ID:{note["id"]}')
               print(f'Title:{note["title"]}')
               print(f'Body:{note["body"]}')
               print(f'Time:{note["time"]}')
               print("\n")

def readNote(data, id):
     for note in data:
          if note["id"] == id:
               print(f'ID:{note["id"]}')
               print(f'Title:{note["title"]}')
               print(f'Body:{note["body"]}')
               print(f'Time:{note["time"]}')
               print("\n")
          else:
               print("There is no note with that id")

def timeNote(data, date):
     date_notes = []
     for note in data:
          note_time = datetime.datetime.strptime(note["time"], '%Y-%m-%d')
          if note_time.date() == date:
               date_notes.append(note)
     return date_notes
          
               
          