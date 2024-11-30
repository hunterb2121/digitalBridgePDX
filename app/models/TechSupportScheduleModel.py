from .BaseModel import BaseModel


class TechSupportScheduleModel(BaseModel):
    table = "tech_support_schedule"

    def __init__(self, id, event_id, end_time):
        self._id = id
        self._event_id = event_id
        self._end_time = end_time

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))
    
    @classmethod
    def find_by_event_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE event_id = %s"
        return cls.get_one(query, (id,))