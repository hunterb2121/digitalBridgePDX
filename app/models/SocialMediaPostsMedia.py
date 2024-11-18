from BaseModel import BaseModel


class SocialMediaPostsMedia(BaseModel):
    table = "social_media_posts_media"

    def __init__(self, id, post_id, post_media_url):
        self._id = id
        self._post_id = post_id
        self._post_media_url = post_media_url

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))