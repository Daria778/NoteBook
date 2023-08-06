import json
import Controller.Controller
def user_input():
    ask = int(input("Chose an option:\n 1 - add and save\n" 
                    "2 - edit\n" 
                    "3 - read \n"
                    "4 - delete\n" 
                    "5 - exit\n "))
    return ask
    
def add ():
    title = str(input("Enter the title of your note: "))
    body = str(input("Enter the body of your note: "))
    
    data = {
  "title": title,
  "body": body
}
    return data

