from .BaseModel import BaseModel


class ClassScheduleModel(BaseModel):
    table = "class_schedule"

    def __init__(self, id, event_id, class_id, end_time, number_seats):
        self._id = id
        self._event_id = event_id
        self._class_id = class_id
        self._end_time = end_time
        self._number_seats = number_seats

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))
    
    @classmethod
    def find_by_event_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE event_id = %s"
        return cls.get_one(query, (id,))
    
    @classmethod
    def find_by_class_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE class_id = %s"
        return cls.get_all(query, (id,))
    
    @classmethod
    def find_by_number_seats(cls, number_seats):
        query = f"SELECT * FROM {cls.table} WHERE number_seats = %s"
        return cls.get_all(query, (number_seats,))
    
    @classmethod
    def get_remaining_seats(cls, number_seats, id):
        query = f"SELECT COUNT(*) FROM {cls.table} INNER JOIN class_registration ON {cls.table}.id = class_registration.schedule_id WHERE {cls.table}.id = %s"
        return cls.get_one(query, (id,)) - number_seats