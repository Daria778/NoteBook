import json


def add(notes, title):
    with open(title, "a") as file:
        json.dump(notes, file)
    print("Запись была обновлена")

def read(data):
     with open (data, "r") as jsfile:    
        notes = json.load(jsfile)
        return notes


    