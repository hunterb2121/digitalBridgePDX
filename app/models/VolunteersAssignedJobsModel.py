from .BaseModel import BaseModel


class VolunteersAssignedJobsModel(BaseModel):
    table = "volunteers_assigned_jobs"

    def __init__(self, volunteer_id, job_id, assigned_date):
        self._volunteer_id = volunteer_id
        self._job_id = job_id
        self._assigned_date = assigned_date

    @classmethod
    def find_by_volunteer_id(cls, volunteer_id):
        query = f"SELECT * FROM {cls.table} WHERE volunteer_id = %s"
        return cls.get_all(query, (volunteer_id,))

    @classmethod
    def find_by_job_id(cls, job_id):
        query = f"SELECT * FROM {cls.table} WHERE job_id = %s"
        return cls.get_all(query, (job_id,))
    
    @classmethod
    def find_by_assigned_date(cls, assigned_date):
        query = f"SELECT * FROM {cls.table} WHERE assigned_date = %s"
        return cls.get_one(query, (assigned_date,))