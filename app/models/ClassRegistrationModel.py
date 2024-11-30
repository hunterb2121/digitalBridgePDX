from .BaseModel import BaseModel


class ClassRegistrationModel(BaseModel):
    table = "class_registration"

    def __init__(self, id, schedule_id, name, email, phone_number):
        self._id = id
        self._schedule_id = schedule_id
        self._name = name
        self._email = email
        self._phone_number = phone_number

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))
    
    @classmethod
    def find_by_schedule_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE schedule_id = %s"
        return cls.get_all(query, (id,))
    
    @classmethod
    def find_by_name(cls, name):
        query = f"SELECT * FROM {cls.table} WHERE name = %s"
        return cls.get_all(query, (name,))
    
    @classmethod
    def find_by_email(cls, email):
        query = f"SELECT * FROM {cls.table} WHERE email = %s"
        return cls.get_all(query, (email,))
    
    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["name", "email", "phone_number"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))