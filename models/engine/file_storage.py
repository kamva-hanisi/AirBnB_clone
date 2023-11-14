#!/usr/bin/python3
"""Module that define class FileStorage"""
import json
import os


class FileStorage:
    """Class Filestorage that serializes instances to JSON and
        deserializes JSON file to instances

        all: returns an __objects
        new: sets in __objects the obj with key <obj class name>.id
        save: serializes __objects to the JSON file(path: __file_path)
        reload: deserializes the JSON file to __objects
    """

    __file_path = 'air.json'
    __objects = {}

    def all(self):
        """method that returns the dictionary __object"""

        return FileStorage.__objects

    def new(self, obj):
        """Sets in __object the obj with key
          """
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""

        with open(FileStorage.__file_path, 'w') as json_data:
            data = {}
            for k, obj in FileStorage.__objects.items():
                data[k] = obj.to_dict()

            json.dump(data, json_data)

    def reload(self):
        """Deserializes the JSON file to __objects"""

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as json_file:
                data = json.load(json_file)
                from models.amenity import Amenity
                from models.base_model import BaseModel
                from models.city import City
                from models.review import Review
                from models.state import State
                from models.place import Place
                from models.user import User
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'BaseModel':
                        class_model = BaseModel
                    elif class_name == 'User':
                        class_model = User
                    elif class_name == 'State':
                        class_model = State
                    elif class_name == 'City':
                        class_model = City
                    elif class_name == 'Amenity':
                        class_model = Amenity
                    elif class_name == 'Place':
                        class_model = Place
                    elif class_name == 'Review':
                        class_model = Review
                    else:
                        class_model = None

                    if class_model:
                        FileStorage.__objects[key] = class_model(**value)
