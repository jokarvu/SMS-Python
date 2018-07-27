from .BaseModel import BaseModel

class Class(BaseModel):
    def __init__(self):
        super().__init__()
        self.table = "classes"
        self.columns = ['name', 'student_number', 'start_at', 'end_at', 'semester_id', 'teacher_id', 'room_id']
    def __del__(self):
        super().__del__()