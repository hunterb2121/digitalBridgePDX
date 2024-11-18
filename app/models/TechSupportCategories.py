from BaseModel import BaseModel


class TechSupportCategories(BaseModel):
    table = "tech_support_categories"

    def __init__(self, id, name, description):
        self._id = id
        self._name = name
        self._description = description

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_name(cls, name):
        query = f"SELECT * FROM {cls.table} WHERE name = %s"
        return cls.get_all(query, (name,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["name"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))