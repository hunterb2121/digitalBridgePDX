from .BaseModel import BaseModel


class TechSupportResourcesModel(BaseModel):
    table = "tech_support_resources"

    def __init__(self, id, title, description, file_path, category_id, created_date):
        self._id = id
        self._title = title
        self._description = description
        self._file_path = file_path
        self._category_id = category_id
        self._created_date = created_date

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_title(cls, title):
        query = f"SELECT * FROM {cls.table} WHERE title = %s"
        return cls.get_one(query, (title,))
    
    @classmethod
    def find_by_category_id(cls, category_id):
        query = f"SELECT * FROM {cls.table} WHERE category_id = %s"
        return cls.get_all(query, (category_id,))
    
    @classmethod
    def find_by_created_date(cls, created_date):
        query = f"SELECT * FROM {cls.table} WHERE created_date = %s"
        return cls.get_all(query, (created_date,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["title"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))