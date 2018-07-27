# Import section
from Model.User import User
from Controller.UserController import UserController

# Main section
while True:
    print("="*50)
    print("{:^50}".format("MAIN MENU - SCHOOL MANAGEMENT SYSTEM"))
    print("{}{:<50}".format(" "*5, "1. Student Management Menu"))
    print("{}{:<50}".format(" "*5, "2. Teacher Management Menu"))
    print("{}{:<50}".format(" "*5, "3. Class Management Menu"))
    print("="*50)
    try:
        command = int(input(">> Enter your command (Enter 0 to exit): "))
    except ValueError:
        print("** WARNING: Invalid command. Please enter number only!")
        continue
    if command == 0:
        exit()
    elif command == 1:
        # User controller
        user = UserController()
        pass
    elif command == 2:
        # Teacher controller
        pass
    elif command == 3:
        # Class controller
        pass
    else:
        print("** WARNING: Your command is invalid. Please try again")