from .BaseModel import BaseModel


class DevicesModel(BaseModel):
    table = "devices"

    def __init__(self, id, device_type, device_manf, device_model, serial_number, condition, date_acquired, acquisition_source, notes, value, current_location, repair_needed, repair_cost_estimate, repair_history):
        self._id = id
        self._device_type = device_type
        self._device_manf = device_manf
        self._device_model = device_model
        self._serial_number = serial_number
        self._condition = condition
        self._date_acquired = date_acquired
        self._acquisition_source = acquisition_source
        self._notes = notes
        self._value = value
        self._current_location = current_location
        self._repair_needed = repair_needed
        self._repair_cost_estimate = repair_cost_estimate
        self._repair_history = repair_history

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_device_type(cls, device_type):
        query = f"SELECT * FROM {cls.table} WHERE device_type = %s"
        return cls.get_all(query, (device_type,))
    
    @classmethod
    def find_by_device_manf(cls, device_manf):
        query = f"SELECT * FROM {cls.table} WHERE device_manf = %s"
        return cls.get_all(query, (device_manf,))
    
    @classmethod
    def find_by_device_model(cls, device_model):
        query = f"SELECT * FROM {cls.table} WHERE device_model = %s"
        return cls.get_all(query, (device_model,))
    
    @classmethod
    def find_by_serial_number(cls, serial_number):
        query = f"SELECT * FROM {cls.table} WHERE serial_number = %s"
        return cls.get_one(query, (serial_number,))
    
    @classmethod
    def find_by_condition(cls, condition):
        query = f"SELECT * FROM {cls.table} WHERE condition = %s"
        return cls.get_all(query, (condition,))
    
    @classmethod
    def find_by_date_acquired(cls, date_acquired):
        query = f"SELECT * FROM {cls.table} WHERE date_acquired = %s"
        return cls.get_all(query, (date_acquired,))
    
    @classmethod
    def find_by_acquisition_source(cls, acquisition_source):
        query = f"SELECT * FROM {cls.table} WHERE acquisition_source = %s"
        return cls.get_all(query, (acquisition_source,))
    
    @classmethod
    def find_by_if_repair_needed(cls):
        query = f"SELECT * FROM {cls.table} WHERE repair_needed = TRUE"
        return cls.get_all(query)
    
    @classmethod
    def find_by_if_no_repair_needed(cls):
        query = f"SELECT * FROM {cls.table} WHERE repair_needed = FALSE"
        return cls.get_all(query)
    
    @classmethod
    def find_by_repair_history(cls, repair_history):
        query = f"SELECT * FROM {cls.table} WHERE repair_history = %s"
        return cls.get_all(query, (repair_history,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["device_type", "device_manf", "device_model", "serial_number", "acquisition_source", "current_location"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))