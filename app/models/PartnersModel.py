from .BaseModel import BaseModel


class PartnersModel(BaseModel):
    table = "partners"

    def __init__(self, id, business_name, contact_person, contact_email, contact_phone, notes):
        self._id = id
        self._business_name = business_name
        self._contact_person = contact_person
        self._contact_email = contact_email
        self._contact_phone = contact_phone
        self._notes = notes

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_business_name(cls, business_name):
        query = f"SELECT * FROM {cls.table} WHERE business_name = %s"
        return cls.get_one(query, (business_name,))
    
    @classmethod
    def find_by_contact_person(cls, contact_person):
        query = f"SELECT * FROM {cls.table} WHERE contact_person = %s"
        return cls.get_one(query, (contact_person,))
    
    @classmethod
    def find_by_contact_email(cls, contact_email):
        query = f"SELECT * FROM {cls.table} WHERE contact_email = %s"
        return cls.get_one(query, (contact_email,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["business_name", "contact_person", "contact_email", "contact_phone"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))