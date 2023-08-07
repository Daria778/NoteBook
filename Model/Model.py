import datetime

def delete(data, id):
        for note in data:
            if note["id"] == id:
                data.remove(note)
            break

def edit(data, id):
     for note in data:
          if note["id"] == id:
                title = str(input("Enter the title of your note: "))
                body = str(input("Enter the body of your note: "))
                time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
                newNote = {"id": id, "title": title, "body": body, "time": time}
                data.append(newNote)
                return data