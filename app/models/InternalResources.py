from BaseModel import BaseModel


class InternalResources(BaseModel):
    table = "internal_resources"

    def __init__(self, id, title, description, file_path, category, date_created):
        self._id = id
        self._title = title
        self._description = description
        self._file_path = file_path
        self._category = category
        self._date_created = date_created

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_title(cls, title):
        query = f"SELECT * FROM {cls.table} WHERE title = %s"
        return cls.get_all(query, (title,))
    
    @classmethod
    def find_by_category(cls, category):
        query = f"SELECT * FROM {cls.table} WHERE category = %s"
        return cls.get_all(query, (category,))
    
    @classmethod
    def find_by_date_created(cls, date_created):
        query = f"SELECT * FROM {cls.table} WHERE date_created = %s"
        return cls.get_all(query, (date_created,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["title", "category"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))