from .BaseModel import BaseModel


class AuditLogsModel(BaseModel):
    table = "audit_logs"

    def __init__(self, id, table_name, record_id, action_type, performed_by, change_details, change_timestamp):
        self._id = id
        self._table_name = table_name
        self._record_id = record_id
        self._action_type = action_type
        self._performed_by = performed_by
        self._change_details = change_details
        self._change_timestamp = change_timestamp

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_table_name(cls, table_name):
        query = f"SELECT * FROM {cls.table} WHERE table_name = %s"
        return cls.get_all(query, (table_name,))
    
    @classmethod
    def find_by_record_id(cls, record_id):
        query = f"SELECT * FROM {cls.table} WHERE record_id = %s"
        return cls.get_all(query, (record_id,))
    
    @classmethod
    def find_by_action_type(cls, action_type):
        query = f"SELECT * FROM {cls.table} WHERE action_type = %s"
        return cls.get_all(query, (action_type,))
    
    @classmethod
    def find_by_performed_by(cls, performed_by):
        query = f"SELECT * FROM {cls.table} WHERE performed_by = %s"
        return cls.get_all(query, (performed_by,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["table_name", "action_type"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))