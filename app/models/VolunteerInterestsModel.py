from .BaseModel import BaseModel


class VolunteerInterestsModel(BaseModel):
    table = "volunteer_interests"

    def __init__(self, volunteer_id, interest_id):
        self._volunteer_id = volunteer_id
        self._interest_id = interest_id

    @classmethod
    def find_by_volunteer(cls, volunteer_id):
        query = f"SELECT * FROM {cls.table} WHERE volunteer_id = %s"
        return cls.get_all(query, (volunteer_id,))

    @classmethod
    def find_by_interest(cls, interest_id):
        query = f"SELECT * FROM {cls.table} WHERE interest_id = %s"
        return cls.get_all(query, (interest_id,))