from .BaseModel import BaseModel


class UserRolesModel(BaseModel):
    table = "user_roles"

    def __init__(self, volunteer_id, role_id, assigned_date):
        self._volunteer_id = volunteer_id
        self._role_id = role_id
        self._assigned_date = assigned_date

    @classmethod
    def find_by_volunteer_id(cls, volunteer_id):
        query = f"SELECT * FROM {cls.table} WHERE volunteer_id = %s"
        return cls.get_all(query, (volunteer_id,))

    @classmethod
    def find_by_role_id(cls, role_id):
        query = f"SELECT * FROM {cls.table} WHERE role_id = %s"
        return cls.get_all(query, (role_id,))
    
    @classmethod
    def find_by_assigned_date(cls, assigned_date):
        query = f"SELECT * FROM {cls.table} WHERE assigned_date = %s"
        return cls.get_one(query, (assigned_date,))