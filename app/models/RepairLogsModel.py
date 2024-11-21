from .BaseModel import BaseModel


class RepairLogsModel(BaseModel):
    table = "repair_logs"

    def __init__(self, id, device_id, technician_id, repair_date, description, cost, status):
        self._id = id
        self._device_id = device_id
        self._technician_id = technician_id
        self._repair_id = repair_date
        self._description = description
        self._cost = cost
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
    def find_by_technician_id(cls, technician_id):
        query = f"SELECT * FROM {cls.table} WHERE technician_id = %s"
        return cls.get_all(query, (technician_id,))
    
    @classmethod
    def find_by_repair_date(cls, repair_date):
        query = f"SELECT * FROM {cls.table} WHERE repair_date = %s"
        return cls.get_all(query, (repair_date,))
    
    @classmethod
    def find_by_status(cls, status):
        query = f"SELECT * FROM {cls.table} WHERE status = %s"
        return cls.get_all(query, (status,))