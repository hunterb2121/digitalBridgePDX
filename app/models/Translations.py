from BaseModel import BaseModel


class Translations(BaseModel):
    table = "translations"

    def __init__(self, id, content_type, content_id, language, fully_translated, translated_date):
        self._id = id
        self._content_type = content_type
        self._content_id = content_id
        self._language = language
        self._fully_translated = fully_translated
        self._translated_date = translated_date

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_content_type(cls, content_type):
        query = f"SELECT * FROM {cls.table} WHERE content_type = %s"
        return cls.get_all(query, (content_type,))
    
    @classmethod
    def find_by_content_id(cls, content_id):
        query = f"SELECT * FROM {cls.table} WHERE content_id = %s"
        return cls.get_one(query, (content_id,))
    
    @classmethod
    def find_by_language(cls, language):
        query = f"SELECT * FROM {cls.table} WHERE language = %s"
        return cls.get_all(query, (language,))
    
    @classmethod
    def find_if_fully_translated(cls):
        query = f"SELECT * FROM {cls.table} WHERE fully_translated = TRUE"
        return cls.get_all(query)
    
    @classmethod
    def find_if_not_fully_translated(cls):
        query = f"SELECT * FROM {cls.table} WHERE fully_translated = FALSE"
        return cls.get_all(query)
    
    @classmethod
    def find_by_translated_date(cls, translated_date):
        query = f"SELECT * FROM {cls.table} WHERE translated_date = %s"
        return cls.get_all(query, (translated_date,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["content_type", "language"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))