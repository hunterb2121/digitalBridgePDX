from .BaseModel import BaseModel


class InternalInventoryModel(BaseModel):
    table = "internal_inventory"

    def __init__(self, id, device_id, purpose, assigned_to, last_assigned, status):
        self._id = id
        self._device_id = device_id
        self._purpose = purpose
        self._assigned_to = assigned_to
        self._last_assigned = last_assigned
        self._status = status

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_device_id(cls, device_id):
        query = f"SELECT * FROM {cls.table} WHERE device_id = %s"
        return cls.get_all(query, (device_id,))
    
    @classmethod
    def find_by_purpose(cls, purpose):
        query = f"SELECT * FROM {cls.table} WHERE purpose = %s"
        return cls.get_all(query, (purpose,))
    
    @classmethod
    def find_by_assigned_to(cls, assigned_to):
        query = f"SELECT * FROM {cls.table} WHERE purpose = %s"
        return cls.get_all(query, (assigned_to,))
    
    @classmethod
    def find_by_last_assigned(cls, last_assigned):
        query = f"SELECT * FROM {cls.table} WHERE last_assigned = %s"
        return cls.get_all(query, (last_assigned,))
    
    @classmethod
    def find_by_status(cls, status):
        query = f"SELECT * FROM {cls.table} WHERE status = %s"
        return cls.get_all(query, (status,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["purpose"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))