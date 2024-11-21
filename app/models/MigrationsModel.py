from .BaseModel import BaseModel


class MigrationsModel(BaseModel):
    table = "migrations"

    def __init__(self, id, migration_name, applied_at):
        self._id = id
        self._migration_name = migration_name
        self._applied_at = applied_at

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_migration_name(cls, migration_name): 
        query = f"SELECT * FROM {cls.table} WHERE migration_name = %s"
        return cls.get_all(query, (migration_name,))

    @classmethod
    def find_by_applied_at(cls, applied_at):
        query = f"SELECT * FROM {cls.table} WHERE applied_at = %s"
        return cls.get_all(query, (applied_at,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["migration_name"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))