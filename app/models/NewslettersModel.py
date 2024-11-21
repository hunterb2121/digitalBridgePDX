from .BaseModel import BaseModel


class NewslettersModel(BaseModel):
    table = "newsletters"

    def __init__(self, id, title, issue_number, file_path, published_date):
        self._id = id
        self._title = title
        self._issue_number = issue_number
        self._file_path = file_path
        self._published_date = published_date

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_title(cls, title):
        query = f"SELECT * FROM {cls.table} WHERE title = %s"
        return cls.get_all(query, (title,))
    
    @classmethod
    def find_by_issue_number(cls, issue_number):
        query = f"SELECT * FROM {cls.table} WHERE issue_number = %s"
        return cls.get_one(query, (issue_number,))
    
    @classmethod
    def find_by_published_date(cls, published_date):
        query = f"SELECT * FROM {cls.table} WHERE published_date = %s"
        return cls.get_all(query, (published_date,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["title"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))