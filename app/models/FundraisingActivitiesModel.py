from .BaseModel import BaseModel


class FundraisingActivitiesModel(BaseModel):
    table = "fundraising_activities"

    def __init__(self, id, title, description, goal_amount, funds_raised, start_date, end_date):
        self._id = id
        self._title = title
        self._description = description
        self._goal_amount = goal_amount
        self._funds_raised = funds_raised
        self._start_date = start_date
        self._end_date = end_date

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_title(cls, title):
        query = f"SELECT * FROM {cls.table} WHERE title = %s"
        return cls.get_one(query, (title,))
    
    @classmethod
    def find_by_start_date(cls, start_date):
        query = f"SELECT * FROM {cls.table} WHERE start_date = %s"
        return cls.get_all(query, start_date)
    
    @classmethod
    def find_by_end_date(cls, end_date):
        query = f"SELECT * FROM {cls.table} WHERE end_date = %s"
        return cls.get_all(query, (end_date,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["title"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))