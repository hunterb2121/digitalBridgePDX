from BaseModel import BaseModel


class PartnerRegistration(BaseModel):
    table = "partner_registration"

    def __init__(self, id, business_name, contact_name, email, phone_number, message, status, submitted_date):
        self._id = id
        self._business_name = business_name
        self._contact_name = contact_name
        self._email = email
        self._phone_number = phone_number
        self._message = message
        self._status = status
        self._submitted_date = submitted_date

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))
    
    @classmethod
    def find_by_business_name(cls, business_name):
        query = f"SELECT * FROM {cls.table} WHERE business_name = %s"
        return cls.get_one(query, (business_name,))
    
    @classmethod
    def find_by_email(cls, email):
        query = f"SELECT * FROM {cls.table} WHERE email = %s"
        return cls.get_one(query, (email,))
    
    @classmethod
    def find_by_status(cls, status):
        query = f"SELECT * FROM {cls.table} WHERE status = %s"
        return cls.get_all(query, (status,))
    
    @classmethod
    def find_by_submitted_date(cls, submitted_date):
        query = f"SELECT * FROM {cls.table} WHERE submitted_date = %s"
        return cls.get_all(query, (submitted_date,))
    
    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["business_name", "contact_name", "email", "phone_number"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))