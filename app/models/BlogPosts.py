from BaseModel import BaseModel


class BlogPosts(BaseModel):
    table = "blog_posts"

    def __init__(self, id, title, author_id, file_path, published_date, is_published):
        self._id = id
        self._title = title
        self._author_id = author_id
        self._file_path = file_path
        self._published_date = published_date
        self._is_published = is_published

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_title(cls, title):
        query = f"SELECT * FROM {cls.table} WHERE title = %s"
        return cls.get_all(query, (title,))
    
    @classmethod
    def find_by_author_id(cls, author_id):
        query = f"SELECT * FROM {cls.table} WHERE author_id = %s"
        return cls.get_all(query, (author_id,))
    
    @classmethod
    def find_by_published_date(cls, published_date):
        query = f"SELECT * FROM {cls.table} WHERE published_date = %s"
        return cls.get_all(query, (published_date,))
    
    @classmethod
    def find_by_is_published(cls):
        query = f"SELECT * FROM {cls.table} WHERE is_published = TRUE"
        return cls.get_all(query)
    
    @classmethod
    def find_by_is_not_published(cls):
        query = f"SELECT * FROM {cls.table} WHERE is_published = FALSE"
        return cls.get_all(query)

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["title"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))