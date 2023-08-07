import View.View
import Model.FileHandler


work = True
def main():
    while work:
        ask = View.View.user_input()
        if ask == 1:
            data = View.View.add()
            note = data[0]
            title = data[1]
            Model.FileHandler.add(note, title)
        elif ask == 2:
            data == View.View.read()
            Model.FileHandler.read(data)
        elif ask == 3:
            data == View.View.delete()
            Model.FileHandler.delete(data)
        elif ask == 4:
            View.View.exit()
            work = False

        
        

