from BaseModel import BaseModel


class Donations(BaseModel):
    table = "donations"

    def __init__(self, id, what_donated, quantity, specific_donation_info, donor_name, donor_email, donor_phone_number, status, notes, donated_date):
        self._id = id
        self._what_donated = what_donated
        self._quantity = quantity
        self._specific_donation_info = specific_donation_info
        self._donor_name = donor_name
        self._donor_email = donor_email
        self._donor_phone_number = donor_phone_number
        self._status = status
        self._notes = notes
        self._donated_date = donated_date

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_what_donated(cls, what_donated):
        query = f"SELECT * FROM {cls.table} WHERE what_donated = %s"
        return cls.get_all(query, (what_donated,))
    
    @classmethod
    def find_by_donor_name(cls, donor_name):
        query = f"SELECT * FROM {cls.table} WHERE donor_name = %s"
        return cls.get_all(query, (donor_name,))
    
    @classmethod
    def find_by_donor_email(cls, donor_email):
        query = f"SELECT * FROM {cls.table} WHERE donor_email = %s"
        return cls.get_all(query, (donor_email,))
    
    @classmethod
    def find_by_status(cls, status):
        query = f"SELECT * FROM {cls.table} WHERE status = %s"
        return cls.get_all(query, (status,))
    
    @classmethod
    def find_by_donated_date(cls, donated_date):
        query = f"SELECT * FROM {cls.table} WHERE donated_date = %s"
        return cls.get_all(query, (donated_date,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["what_donated", "donor_name", "donor_email", "donor_phone_number"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))