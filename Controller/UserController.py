import bcrypt
from Model.User import User
from View.UserView import UserView

class UserController:
    def __init__(self):
        self.model = User()
        self.view = UserView()
        self.menu()
    def menu(self):
        while True:
        # Render User Menu and get command value
            command = self.view.menu()
            if command == 0:
                return
            elif command == 1:
                self.addUser()
            elif command == 4:
                self.deleteUser()
            elif command == 5:
                self.listUser()
            else:
                pass
    def listUser(self):
        res = self.model.select()
        self.view.listUser(res)
    def addUser(self):
        data = self.view.addUser()
        data['password'] = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        if self.model.insert(data):
            print("OK")
        else:
            print("Failed")
    def deleteUser(self):
        data = self.view.deleteUser()
        if data == 'cancelled':
            return
        else:
            if self.model.delete(data):
                print("Deleted")
            else:
                print("Failed")
