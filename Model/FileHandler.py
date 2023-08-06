import json

def add(data):
    with open("note.json", "a") as file:
        file.writelines(data)
        json.dump(data, file, indent = 3)
    print("Запись была обновлена")