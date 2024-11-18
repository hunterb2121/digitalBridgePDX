from BaseModel import BaseModel


class TechSupportTickets(BaseModel):
    table = "tech_support_tickets"

    def __init__(self, id, requester_name, requester_email, requester_phone, type_of_support, problem_description, category_id, status, assigned_to, submitted_date, resolved_date):
        self._id = id
        self._requester_name = requester_name
        self._requester_email = requester_email
        self._requester_phone = requester_phone
        self._type_of_support = type_of_support
        self._problem_description = problem_description
        self._category_id = category_id
        self._status = status
        self._assigned_to = assigned_to
        self._submitted_date = submitted_date
        self._resolved_date = resolved_date

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_requester_name(cls, requester_name):
        query = f"SELECT * FROM {cls.table} WHERE requester_name = %s"
        return cls.get_all(query, (requester_name,))
    
    @classmethod
    def find_by_requester_email(cls, requester_email):
        query = f"SELECT * FROM {cls.table} WHERE requester_email = %s"
        return cls.get_all(query, (requester_email,))
    
    @classmethod
    def find_by_type_of_support(cls, type_of_support):
        query = f"SELECT * FROM {cls.table} WHERE type_of_support = %s"
        return cls.get_all(query, (type_of_support,))
    
    @classmethod
    def find_by_category_id(cls, category_id):
        query = f"SELECT * FROM {cls.table} WHERE category_id = %s"
        return cls.get_all(query, (category_id,))
    
    @classmethod
    def find_by_status(cls, status):
        query = f"SELECT * FROM {cls.table} WHERE status = %s"
        return cls.get_all(query, (status,))
    
    @classmethod
    def find_by_assigned_to(cls, assigned_to):
        query = f"SELECT * FROM {cls.table} WHERE assigned_to = %s"
        return cls.get_all(query, (assigned_to,))
    
    @classmethod
    def find_by_submitted_date(cls, submitted_date):
        query = f"SELECT * FROM {cls.table} WHERE submitted_date = %s"
        return cls.get_all(query, (submitted_date,))
    
    @classmethod
    def find_by_resolved_date(cls, resolved_date):
        query = f"SELECT * FROM {cls.table} WHERE resolved_date = %s"
        return cls.get_all(query, (resolved_date,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["requester_name", "requester_email", "requester_phone"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))