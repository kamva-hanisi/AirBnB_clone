#!/usr/bin/python3
"""Module for Base class Contains the Base class for the AirBnB clone"""

from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """Class for base model"""

    def __init__(self, *args, **kwargs):
        """Initialization of a class Basemodel"""

        if args:
            raise TypeError('Positional arguments is not accepted(*args)')
        elif kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key == '__class__':
                    pass
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation
        of an instance."""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Saves the current instance of the model"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns dictionary representation of instance"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
