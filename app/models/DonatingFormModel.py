from .BaseModel import BaseModel


class DonatingFormModel(BaseModel):
    table = "donating_form"

    def __init__(self, id, name, email, phone_number, what_donating, additional_information, status, submitted_date):
        self._id = id
        self._name = name
        self._email = email
        self._phone_number = phone_number
        self._what_donating = what_donating
        self._additional_information = additional_information
        self._status = status
        self._submitted_date = submitted_date

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_email(cls, email):
        query = f"SELECT * FROM {cls.table} WHERE email = %s"
        return cls.get_all(query, (email,))

    @classmethod
    def find_by_status(cls, status):
        query = f"SELECT * FROM {cls.table} WHERE status = %s"
        return cls.get_all(query, (status,))
    
    @classmethod
    def find_by_what_donating(cls, what_donating):
        query = f"SELECT * FROM {cls.table} WHERE what_donating = %s"
        return cls.get_all(query, (what_donating,))
    
    @classmethod
    def find_by_submitted_date(cls, submitted_date):
        query = f"SELECT * FROM {cls.table} WHERE submitted_date = %s"
        return cls.get_all(query, (submitted_date,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["name", "email", "phone_number"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))