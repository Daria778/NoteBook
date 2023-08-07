import json
def save(notes, title):
    with open(title, "w") as file:
        json.dump(notes, file)
    print("The note has been saved")

def read(title):
     with open (title, "r") as file:    
        notes = json.load(file)
        return notes


    