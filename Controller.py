import Model
import FileHandler
import View



def main():
    work = True
    file = "notes.json"
    data = []

    while work:
        ask = View.user_input()
        if ask == 1:
            data = View.add(data)
            FileHandler.save(data, file)
        elif ask == 2:
            ids = View.edit()
            data = Model.edit(data, ids)
            FileHandler.save(data, file)
        elif ask == 3:
            data = FileHandler.read(file)
            data = Model.sort(data)
            Model.printNotes(data)

        elif ask == 4:
            request = View.delete()
            pop = Model.delete(data, request)
            FileHandler.save(pop, file)
        elif ask == 5:
            View.exit()
            work = False
        else:
            print("Try again")
            main()
        
main()        

