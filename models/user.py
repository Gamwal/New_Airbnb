#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    def to_dict(self):
        self.__dict__.update({'__class__': __class__.__name__, 'updated_at': self.updated_at.isoformat(), 'created_at': self.created_at.isoformat()})
        return self.__dict__