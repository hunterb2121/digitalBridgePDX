from BaseModel import BaseModel


class SocialMediaPosts(BaseModel):
    table = "social_media_posts"

    def __init__(self, id, platform, post_content, post_date, metrics):
        self._id = id
        self._platform = platform
        self._post_content = post_content
        self._post_date = post_date
        self._metrics = metrics

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_platform(cls, platform):
        query = f"SELECT * FROM {cls.table} WHERE platform = %s"
        return cls.get_all(query, (platform,))
    
    @classmethod
    def find_by_post_date(cls, post_date):
        query = f"SELECT * FROM {cls.table} WHERE post_date = %s"
        return cls.get_all(query, (post_date,))

    @classmethod
    def search_by_field_keyword(cls, field, keyword):
        allowed_fields = ["platform"]
        if field not in allowed_fields:
            raise ValueError(f"Invalid field: {field}")
        
        query = f"SELECT * FROM {cls.table} WHERE {field} LIKE %s"
        return cls.get_all(query, (f"%{keyword}%",))