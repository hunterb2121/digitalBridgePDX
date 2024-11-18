from BaseModel import BaseModel


class NewsletterTags(BaseModel):
    table = "newsletter_tags"

    def __init__(self, newsletter_id, tag_id):
        self._newsletter_id = newsletter_id
        self._tag_id = tag_id

    @classmethod
    def find_by_newsletter_id(cls, newsletter_id):
        query = f"SELECT * FROM {cls.table} WHERE newsletter_id = %s"
        return cls.get_one(query, (newsletter_id,))

    @classmethod
    def find_by_tag_id(cls, tag_id):
        query = f"SELECT * FROM {cls.table} WHERE tag_id = %s"
        return cls.get_all(query, (tag_id,))