from .BaseModel import BaseModel


class VolunteerJobsModel(BaseModel):
    table = "volunteer_jobs"

    def __init__(self, id, title, description):
        self._id = id
        self._title = title
        self._description = description

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))
    
    @classmethod
    def find_by_title(cls, title):
        query = f"SELECT * FROM {cls.table} WHERE title = %s"
        return cls.get_one(query, (title,))
    
    @classmethod
    def search_title(cls, keyword):
        query = f"SELECT * FROM {cls.table} WHERE title LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))