from .BaseModel import BaseModel


class PostTagsModel(BaseModel):
    table = "post_tags"

    def __init__(self, post_id, tag_id):
        self._post_id = post_id
        self._tag_id = tag_id

    @classmethod
    def find_by_post_id(cls, post_id):
        query = f"SELECT * FROM {cls.table} WHERE post_id = %s"
        return cls.get_one(query, (post_id,))

    @classmethod
    def find_by_tag_id(cls, tag_id):
        query = f"SELECT * FROM {cls.table} WHERE tag_id = %s"
        return cls.get_all(query, (tag_id,))