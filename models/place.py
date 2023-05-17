#!/usr/bin/python3

from models.base_model import BaseModel


class Place(BaseModel):
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""


    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    def to_dict(self):
        self.__dict__.update({'__class__': __class__.__name__, 'updated_at': self.updated_at.isoformat(), 'created_at': self.created_at.isoformat()})
        return self.__dict__