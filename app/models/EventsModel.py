from datetime import date

from .BaseModel import BaseModel


class EventsModel(BaseModel):
    table = "events"

    def __init__(self, id, title, description, date, time, location):
        self._id = id
        self._title = title
        self._description = description
        self._date = date
        self._time = time
        self._location = location

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_title(cls, title):
        query = f"SELECT * FROM {cls.table} WHERE title = %s"
        return cls.get_all(query, (title,))
    
    @classmethod
    def find_by_date(cls, date):
        query = f"SELECT * FROM {cls.table} WHERE date = %s"
        return cls.get_all(query, (date,))
    
    @classmethod
    def find_by_location(cls, location):
        query = f"SELECT * FROM {cls.table} WHERE location = %s"
        return cls.get_all(query, (location,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["title", "date", "time", "location"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))
    
    @classmethod
    def get_all_future_tech_support_events(cls):
        today = date.today()

        query = f"""
        SELECT {cls.table}.id, title, description, date, time, location, end_time FROM {cls.table} 
        INNER JOIN tech_support_schedule ON {cls.table}.id = tech_support_schedule.event_id
        WHERE date >= %s
        ORDER BY date ASC
        """
        return cls.get_all(query, (today,))
    
    @classmethod
    def get_all_future_classes_with_remaining_seats(cls):
        today = date.today()

        query = f"""
        SELECT {cls.table}.id, {cls.table}.title, {cls.table}.description, {cls.table}.date, {cls.table}.time, {cls.table}.location, cs.end_time, cs.number_seats, cs.id, cs.number_seats - COALESCE(COUNT(cr.schedule_id), 0) AS remaining_seats FROM {cls.table}
        INNER JOIN class_schedule cs ON {cls.table}.id = cs.event_id
        LEFT JOIN class_registration cr ON cs.id = cr.schedule_id
        WHERE {cls.table}.date >= %s
        GROUP BY {cls.table}.id, cs.id
        ORDER BY {cls.table}.date ASC
        """
        return cls.get_all(query, (today,))