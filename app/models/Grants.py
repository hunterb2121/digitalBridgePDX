from BaseModel import BaseModel


class Grants(BaseModel):
    table = "grants"

    def __init__(self, id, title, description, submitted_date, status, amount_requested, amount_awarded):
        self._id = id
        self._title = title
        self._description = description
        self._submitted_date = submitted_date
        self._status = status
        self._amount_requested = amount_requested
        self._amount_awarded = amount_awarded

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_title(cls, title):
        query = f"SELECT * FROM {cls.table} WHERE title = %s"
        return cls.get_one(query, (title,))
    
    @classmethod
    def find_by_submitted_date(cls, submitted_date):
        query = f"SELECT * FROM {cls.table} WHERE submitted_date = %s"
        return cls.get_all(query, (submitted_date,))
    
    @classmethod
    def find_by_status(cls, status):
        query = f"SELECT * FROM {cls.table} WHERE status = %s"
        return cls.get_all(query, (status,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["title"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))