class ClassRecordings:
    def __init__(self, id, title, description, file_path, date_recorded, tags, duration):
        self._id = id
        self._title = title
        self._description = description
        self._file_path = file_path
        self._date_recorded = date_recorded
        self._tags = tags
        self._duration = duration

    @property
    def id(self):
        return self._id
    
    @property
    def title(self):
        return self._title
    
    @property
    def description(self):
        return self._description
    
    @property
    def file_path(self):
        return self._file_path
    
    @property
    def date_recorded(self):
        return self._date_recorded
    
    @property
    def tags(self):
        return self._tags
    
    @property
    def duration(self):
        return self._duration
    
    @title.setter
    def title(self, new_title):
        self._title = new_title

    @description.setter
    def description(self, new_description):
        self._description = new_description

    @file_path.setter
    def file_path(self, new_file_path):
        self._file_path = new_file_path

    @tags.setter
    def tags(self, new_tags):
        self._tags = new_tags

    @duration.setter
    def duration(self, new_duration):
        self._duration = new_duration