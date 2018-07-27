import re

class UserView:
    def __init__(self):
        pass
    def menu(self):
        while True:
            print("="*50)
            print("{:^50}".format("STUDENT MENU - SCHOOL MANAGEMENT SYSTEM"))
            print("{}{:<50}".format(" "*5, "0. Back"))
            print("{}{:<50}".format(" "*5, "1. Add User"))
            print("{}{:<50}".format(" "*5, "2. Search User"))
            print("{}{:<50}".format(" "*5, "3. Edit User"))
            print("{}{:<50}".format(" "*5, "4. Delete User"))
            print("{}{:<50}".format(" "*5, "5. List User"))
            print("="*50)
            try:
                command = int(input(">> Enter your command: "))
            except ValueError:
                print("** WARNING: Invalid command. Please enter number only!")
                continue
            return command
    def listUser(self, data):
        if not data:
            print("No data was found!")
            return
        print("+{}+{}+{}+{}+{}+".format("-"*7, "-"*25, "-"*30, "-"*25, "-"*25))
        print("|{:^7}".format("ID"), end= "")
        print("|{:^25}".format("Name"), end = "")
        print("|{:^30}".format("Email"), end = "")
        print("|{:^25}".format("Created"), end = "")
        print("|{:^25}|".format("Updated"))
        print("+{}+{}+{}+{}+{}+".format("-"*7, "-"*25, "-"*30, "-"*25, "-"*25))
        for value in data:
            print("|{:<7}".format(value["id"]), end= "")
            print("|{:<25}".format(value["name"]), end = "")
            print("|{:<30}".format(value["email"]), end = "")
            print("|{:^25}".format(value["created_at"].strftime("%Y-%m-%d %H:%M:%S")), end = "")
            print("|{:^25}|".format(value["updated_at"].strftime("%Y-%m-%d %H:%M:%S")))
            print("+{}+{}+{}+{}+{}+".format("-"*7, "-"*25, "-"*30, "-"*25, "-"*25))
    def addUser(self):
        while True:
            username = str(input(">> Enter username: "))
            if re.match(r"^[a-zA-Z0-9\_\.]{6,24}", username):
                break
            else:
                print("** WARNING: Username must contain letter, digit only!")
        while True:
            email = str(input(">> Enter user's email: "))
            if re.match(r"^[a-zA-Z0-9\.\_]+@[a-z0-9]+\.[a-z]+$", email):
                break
            else:
                print("** WARNING: You have entered an invalid email")
        while True:
            password = str(input(">> Enter user's password: "))
            if re.match(r"^[a-zA-Z0-9\.\$\\\%\^\&\@\!]{6,32}$", password):
                break
            else:
                print("** WARNING: Password does not match requirement")
        return {"name" : username, "email": email, "password": password}
    def deleteUser(self):
        while True:
            try:
                choice = int(input("By which you want to delete user? (1 - ID, 2 - Name, 3 - Email): "))
            except ValueError:
                print("** WARNING: Invalid command!")
                continue
            if choice == 0:
                return 'cancelled'
            elif choice == 1:
                while True:
                    try:
                        userid = int(input(">> Enter user's id that you want to delete: "))
                    except ValueError:
                        print("** WARNING: Invalid command!")
                        continue
                    if userid != 0:
                        return {'id' : userid}
                    else:
                        return 'cancelled'
            elif choice == 2:
                name = str(input(">> Enter username that you want to  delete: "))
                if name != str(0):
                    return {'name' : name}
                else:
                    return 'cancelled'
            elif choice == 3:
                while True:
                    email = str(input(">> Enter user's email that you want to delete: "))
                    if email == str(0):
                        return 'cancelled'
                    elif re.match(r"^[a-zA-Z0-9\.\_]+@[a-z0-9]+\.[a-z]+$", email):
                        break
                    else:
                        print("** WARNING: Please enter a valid email")
                return {'email': email}
            else:
                print("** WARNING: Please enter a valid choice or 0 to cancel")