from BaseModel import BaseModel


class Classes(BaseModel):
    table = "classes"

    def __init__(self, id, title, description):
        self._id = id
        self._title = title
        self._description = description

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_title(cls, title):
        query = f"SELECT * FROM {cls.table} WHERE title = %s"
        return cls.get_all(query, (title,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["title"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))