from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from ..utils.validation import password_complexity_validation
from BaseModel import BaseModel


class Volunteers(BaseModel, UserMixin):
    table = "volunteers"

    def __init__(self, id, name, email, phone_number, password_hash, availability, availability_notes, skills, volunteer_since):
        self._id = id
        self._name = name
        self._email = email
        self._phone_number = phone_number
        self._password_hash = password_hash
        self._availability = availability
        self._availability_notes = availability_notes
        self._skills = skills
        self._volunteer_since = volunteer_since

    def get_id(self):
        return str(self._id)
    
    @staticmethod
    def authenticate(email, password):
        volunteer = Volunteers.find_by_email(email)
        if volunteer and check_password_hash(volunteer["_password_hash:"], password):
            return volunteer
        return None

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_name(cls, name):
        query = f"SELECT * FROM {cls.table} WHERE name = %s"
        return cls.get_all(query, (name,))
    
    @classmethod
    def find_by_email(cls, email):
        query = f"SELECT * FROM {cls.table} WHERE email = %s"
        return cls.get_one(query, (email,))
    
    @classmethod
    def find_by_volunteer_since(cls, volunteer_since):
        query = f"SELECT * FROM {cls.table} WHERE volunteer_since = %s"
        return cls.get_all(query, (volunteer_since,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["name", "email", "phone_number", "availability"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))
    
    @staticmethod
    def create_hash(password):
        if not password_complexity_validation(password):
            raise ValueError("Password not complex enough")
        
        return generate_password_hash(password)
    
    @staticmethod
    def check_hash(hash, password):
        return check_password_hash(hash, password)