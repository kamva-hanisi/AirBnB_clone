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
          cls_name, obj_id = key.split('.')
          if cls_name == 'BaseModel':
            cls = BaseModel
          elif cls_name == 'User':
            cls = User
          elif cls_name == 'State':
            cls = State
          elif cls_name == 'City':
            cls = City
          elif cls_name == 'Amenity':
            cls = Amenity
          elif cls_name == 'Place':
            cls = Place
          elif cls_name == 'Review':
            cls = Review
          else:
            cls = None

          if cls:
            FileStorage.__objects[key] = cls(**value)
    else:
      pass
