from BaseModel import BaseModel

class AccessibilityRequests(BaseModel):
    table = "accessibility_requests"

    def __init__(self, id, resource_id, request_type, description, request_date, finished_date):
        self._id = id
        self._resource_id = resource_id
        self._request_type = request_type
        self._description = description
        self._request_date = request_date
        self._finished_date = finished_date

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_resource_id(cls, resource_id):
        query = f"SELECT * FROM {cls.table} WHERE resource_id = %s"
        return cls.get_all(query, (resource_id,))
    
    @classmethod
    def find_by_request_type(cls, request_type):
        query = f"SELECT * FROM {cls.table} WHERE request_type = %s"
        return cls.get_one(query, (request_type,))
    
    @classmethod
    def find_by_request_date(cls, request_date):
        query = f"SELECT * FROM {cls.table} WHERE request_date = %s"
        return cls.get_all(query, (request_date,))
    
    @classmethod
    def find_by_finished_date(cls, finished_date):
        query = f"SELECT * FROM {cls.table} WHERE finished_date = %s"
        return cls.get_all(query, finished_date)

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["request_type"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))