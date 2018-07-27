from .BaseModel import BaseModel

class User(BaseModel):
    def __init__(self):
        super().__init__()
        self.table = "users"
        self.columns = ['name', 'email', 'password']
        self.hidden = ['password']
    def __del__(self):
        super().__del__()