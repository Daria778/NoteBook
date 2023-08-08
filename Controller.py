import Model
import FileHandler
import View



def main():
    work = True
    file = "notes.json"
    data = []

    while work:
        ask = View.user_input()
        print()
        if ask == 1:
            data = View.add(data)
            FileHandler.save(data, file)
            print()
        elif ask == 2:
            ids = View.edit()
            data = Model.edit(data, ids)
            FileHandler.save(data, file)
            print()
        elif ask == 3:
            data = FileHandler.read(file)
            data = Model.sort(data)
            Model.printNotes(data)
            print()
        elif ask == 4:
            idp = View.readNote()
            print()
            Model.readNote(data, idp)
            print()
        elif ask == 5:
            data = FileHandler.read(file)
            t = View.time()
            f = Model.timeNote(data, t)
            Model.printNotes(f)
        elif ask == 6:
            request = View.delete()
            pop = Model.delete(data, request)
            FileHandler.save(pop, file)
            print()
        elif ask == 7:
            View.exit()
            work = False
            print()
        else:
            print("Try again")
            main()
        
main()        

