from .BaseModel import BaseModel


class ClassTagsModel(BaseModel):
    table = "class_tags"

    def __init__(self, class_id, tag_id):
        self._class_id = class_id
        self._tag_id = tag_id

    @classmethod
    def find_by_class_id(cls, class_id):
        query = f"SELECT * FROM {cls.table} WHERE class_id = %s"
        return cls.get_all(query, (class_id,))

    @classmethod
    def find_by_tag_id(cls, tag_id):
        query = f"SELECT * FROM {cls.table} WHERE tag_id = %s"
        return cls.get_all(query, (tag_id,))