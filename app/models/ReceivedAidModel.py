from .BaseModel import BaseModel


class ReceivedAidModel(BaseModel):
    table = "received_aid"

    def __init__(self, id, name, email, phone_number, what_received, notes, date_aid_received):
        self._id = id
        self._name = name
        self._email = email
        self._phone_number = phone_number
        self._what_received = what_received
        self._notes = notes
        self._date_aid_received = date_aid_received

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
        return cls.get_all(query, (email,))
    
    @classmethod
    def find_by_what_received(cls, what_received):
        query = f"SELECT * FROM {cls.table} WHERE what_received = %s"
        return cls.get_all(query, (what_received,))
    
    @classmethod
    def find_by_date_aid_received(cls, date_aid_received):
        query = f"SELECT * FROM {cls.table} WHERE date_aid_received = %s"
        return cls.get_all(query, (date_aid_received,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["name", "email", "phone_number"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))