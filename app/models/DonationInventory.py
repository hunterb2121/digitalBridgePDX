from BaseModel import BaseModel


class DonationInventory(BaseModel):
    table = "donation_inventory"

    def __init__(self, id, device_id, recipient, donation_information, when_donated):
        self._id = id
        self._device_id = device_id
        self._recipient = recipient
        self._donation_information = donation_information
        self._when_donated = when_donated

    @classmethod
    def find_by_id(cls, id):
        query = f"SELECT * FROM {cls.table} WHERE id = %s"
        return cls.get_one(query, (id,))

    @classmethod
    def find_by_device_id(cls, device_id):
        query = f"SELECT * FROM {cls.table} WHERE device_id = %s"
        return cls.get_all(query, (device_id,))
    
    @classmethod
    def find_by_recipient(cls, recipient):
        query = f"SELECT * FROM {cls.table} WHERE recipient = %s"
        return cls.get_all(query, (recipient,))
    
    @classmethod
    def find_by_donation_information(cls, donation_information):
        query = f"SELECT * FROM {cls.table} WHERE donation_information = %s"
        return cls.get_all(query, (donation_information,))
    
    @classmethod
    def find_by_when_donated(cls, when_donated):
        query = f"SELECT * FROM {cls.table} WHERE when_donated = %s"
        return cls.get_all(query, (when_donated,))