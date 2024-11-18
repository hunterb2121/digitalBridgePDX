from BaseModel import BaseModel


class EventVolunteers(BaseModel):
    table = "event_volunteers"

    def __init__(self, event_id, volunteer_id, role, assignment_date):
        self._event_id = event_id
        self._volunteer_id = volunteer_id
        self._role = role
        self._assignment_date = assignment_date

    @classmethod
    def find_by_event_id(cls, event_id):
        query = f"SELECT * FROM {cls.table} WHERE event_id = %s"
        return cls.get_all(query, (event_id,))
    
    @classmethod
    def find_by_volunteer_id(cls, volunteer_id):
        query = f"SELECT * FROM {cls.table} WHERE volunteer_id = %s"
        return cls.get_all(query, (volunteer_id,))
    
    @classmethod
    def find_by_assignment_date(cls, assignment_date):
        query = f"SELECT * FROM {cls.table} WHERE assignment_date = %s"
        return cls.get_all(query, (assignment_date,))
    
    @classmethod
    def find_by_event_id_role(cls, event_id, role):
        query = f"SELECT * FROM {cls.table} WHERE event_id = %s AND role = %s"
        return cls.get_all(query, (event_id, role,))