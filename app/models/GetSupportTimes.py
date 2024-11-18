from BaseModel import BaseModel


class GetSupportTimes(BaseModel):
    table = "get_support_times"

    def __init__(self, id, support_form_id, morning, afternoon, evening):
        self._id = id
        self._support_form_id = support_form_id
        self._morning = morning
        self._afternoon = afternoon
        self._evening = evening

    @classmethod
    def get_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))
    
    @classmethod
    def get_morning_times(cls):
        query = f"SELECT * FROM {cls.table} WHERE morning = TRUE"
        return cls.get_all(query)
    
    @classmethod
    def get_afternoon_times(cls):
        query = f"SELECT * FROM {cls.table} WHERE afternoon = TRUE"
        return cls.get_all(query)
    
    @classmethod
    def get_evening_times(cls):
        query = f"SELECT * FROM {cls.table} WHERE evening = TRUE"
        return cls.get_all(query)
    
    @classmethod
    def get_times_by_support_form_id(cls, support_form_id):
        query = f"SELECT * FROM {cls.table} WHERE support_form_id = %s"
        return cls.get_one(query, (support_form_id,))