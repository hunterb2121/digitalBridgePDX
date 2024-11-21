from .BaseModel import BaseModel


class VolunteersAssignmentsModel(BaseModel):
    table = "volunteers_assignments"

    def __init__(self, volunteer_id, assignment_id, assigned_date):
        self._volunteer_id = volunteer_id
        self._assignment_id = assignment_id
        self._assigned_date = assigned_date

    @classmethod
    def find_by_volunteer_id(cls, volunteer_id):
        query = f"SELECT * FROM {cls.table} WHERE volunteer_id = %s"
        return cls.get_all(query, (volunteer_id,))

    @classmethod
    def find_by_assignment_id(cls, assignment_id):
        query = f"SELECT * FROM {cls.table} WHERE assignment_id = %s"
        return cls.get_all(query, (assignment_id,))

    @classmethod
    def find_by_assigned_date(cls, assigned_date):
        query = f"SELECT * FROM {cls.table} WHERE assigned_date = %s"
        return cls.get_all(query, (assigned_date,))