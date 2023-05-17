#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs):
        from models import storage
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k in ['updated_at','created_at']:
                    setattr(self, k, datetime.fromisoformat(v))
                elif k not in ['__class__']:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        storage.save()
        storage.reload()
        
    def to_dict(self):
        self.__dict__.update({'__class__': __class__.__name__, 'updated_at': self.updated_at.isoformat(), 'created_at': self.created_at.isoformat()})
        return self.__dict__