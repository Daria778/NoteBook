import Model
import FileHandler
import View



def main():
    work = True
    file = "notes.json"
    data = []

    while work:
        ask = View.user_input()
        print("\n")
        if ask == 1:
            print("\n")
            data = View.add(data)
            FileHandler.save(data, file)
        elif ask == 2:
            print("\n")
            ids = View.edit()
            data = Model.edit(data, ids)
            FileHandler.save(data, file)
        elif ask == 3:
            print("\n")
            data = FileHandler.read(file)
            data = Model.sort(data)
            Model.printNotes(data)

        elif ask == 4:
            print("\n")
            request = View.delete()
            pop = Model.delete(data, request)
            FileHandler.save(pop, file)
        elif ask == 5:
            print("\n")
            View.exit()
            work = False
        else:
            print("\n")
            print("Try again")
            main()
        
main()        

