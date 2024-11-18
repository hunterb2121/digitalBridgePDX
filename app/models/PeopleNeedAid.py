from BaseModel import BaseModel


class PeopleNeedAid(BaseModel):
    table = "people_need_aid"

    def __init__(self, id, name, email, phone_number, whats_needed, yearly_income, additional_information, place_in_queue, status, submitted_date):
        self._id = id
        self._name = name
        self._email = email
        self._phone_number = phone_number
        self._whats_needed = whats_needed
        self._yearly_income = yearly_income
        self._additional_information = additional_information
        self._place_in_queue = place_in_queue
        self._status = status
        self._submitted_date = submitted_date

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
    def find_by_whats_needed(cls, whats_needed):
        query = f"SELECT * FROM {cls.table} WHERE whats_needed = %s"
        return cls.get_all(query, (whats_needed,))
    
    @classmethod
    def find_by_yearly_income(cls, yearly_income):
        query = f"SELECT * FROM {cls.table} WHERE yearly_income = %s"
        return cls.get_all(query, (yearly_income,))
    
    @classmethod
    def find_by_place_in_queue(cls, place_in_queue):
        query = f"SELECT * FROM {cls.table} WHERE place_in_queue = %s"
        return cls.get_one(query, (place_in_queue,))
    
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
        allowed_fields = ["name", "email", "phone_number", "whats_needed", "yearly_income", "place_in_queue"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))