from BaseModel import BaseModel


class Assignments(BaseModel):
    table = "assignments"

    def __init__(self, id, title, task_type, description, assignment_date, completion_date):
        self._id = id
        self._title = title
        self._task_type = task_type
        self._description = description
        self._assignment_date = assignment_date
        self._completion_date = completion_date

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))
    
    @classmethod
    def find_by_title(cls, title):
        query = f"SELECT * FROM {cls.table} WHERE title = %s"
        return cls.get_one(query, (title,))

    @classmethod
    def find_by_task_type(cls, task_type):
        query = f"SELECT * FROM {cls.table} WHERE task_type = %s"
        return cls.get_all(query, (task_type,))
    
    @classmethod
    def find_by_assignment_date(cls, assignment_date):
        query = f"SELECT * FROM {cls.table} WHERE assignment_date = %s"
        return cls.get_all(query, (assignment_date,))
    
    @classmethod
    def find_by_completion_date(cls, completion_date):
        query = f"SELECT * FROM {cls.table} WHERE completion_date = %s"
        return cls.get_all(query, (completion_date,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["title", "task_type"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))
    