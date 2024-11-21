from .BaseModel import BaseModel


class ClassRecordingsModel(BaseModel):
    table = "class_recordings"

    def __init__(self, id, title, description, file_path, date_recorded, duration):
        self._id = id
        self._title = title
        self._description = description
        self._file_path = file_path
        self._date_recorded = date_recorded
        self._duration = duration

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_title(cls, title):
        query = f"SELECT * FROM {cls.table} WHERE title = %s"
        return cls.get_all(query, (title,))
    
    @classmethod
    def find_by_date_recorded(cls, date_recorded):
        query = f"SELECT * FROM {cls.table} WHERE date_recorded = %s"
        return cls.get_all(query, (date_recorded,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["title"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))