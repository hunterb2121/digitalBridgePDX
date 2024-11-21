from .BaseModel import BaseModel


class TechSupportNotesModel(BaseModel):
    table = "tech_support_notes"

    def __init__(self, id, request_id, note_author, note_text, note_date):
        self._id = id
        self._request_id = request_id
        self._note_author = note_author
        self._note_text = note_text
        self._note_date = note_date

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_request_id(cls, request_id):
        query = f"SELECT * FROM {cls.table} WHERE request_id = %s"
        return cls.get_all(query, (request_id,))
    
    @classmethod
    def find_by_note_author(cls, note_author):
        query = f"SELECT * FROM {cls.table} WHERE note_author = %s"
        return cls.get_all(query, (note_author,))
    
    @classmethod
    def find_by_note_date(cls, note_date):
        query = f"SELECT * FROM {cls.table} WHERE note_date = %s"
        return cls.get_all(query, (note_date,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["note_author"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))