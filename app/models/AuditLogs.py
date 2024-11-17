class AuditLogs:
    def __init__(self, id, table_name, record_id, action_type, performed_by, change_details, change_timestamp):
        self._id = id
        self._table_name = table_name
        self._record_id = record_id
        self._action_type = action_type
        self._performed_by = performed_by
        self._change_details = change_details
        self._change_timestamp = change_timestamp

    @property
    def id(self):
        return self._id
    
    @property
    def table_name(self):
        return self._table_name
    
    @property
    def record_id(self):
        return self._record_id
    
    @property
    def action_type(self):
        return self._action_type
    
    @property
    def performed_by(self):
        return self._performed_by
    
    @property
    def change_details(self):
        return self._change_details
    
    @property
    def change_timestamp(self):
        return self._change_timestamp