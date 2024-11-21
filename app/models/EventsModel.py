from .BaseModel import BaseModel


class EventsModel(BaseModel):
    table = "events"

    def __init__(self, id, title, description, date, time, location):
        self._id = id
        self._title = title
        self._description = description
        self._date = date
        self._time = time
        self._location = location

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_title(cls, title):
        query = f"SELECT * FROM {cls.table} WHERE title = %s"
        return cls.get_all(query, (title,))
    
    @classmethod
    def find_by_date(cls, date):
        query = f"SELECT * FROM {cls.table} WHERE date = %s"
        return cls.get_one(query, (date,))
    
    @classmethod
    def find_by_location(cls, location):
        query = f"SELECT * FROM {cls.table} WHERE location = %s"
        return cls.get_all(query, (location,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["title", "date", "time", "location"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))