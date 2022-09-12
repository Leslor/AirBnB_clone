#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from importlib import reload
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, cls=None):
        """Deletes a instance"""
        if (cls):
            FileStorage.__objects.pop("{}.{}".format(
                cls.__class__.name__, cls.id))

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if (cls):
            N = cls.__name__
            d = list(filter(lambda x: x.__class__.__name__ == N,
                            FileStorage.__objects.values()))
            return {"{}.{}".format(N, i.id): i for i in d}
        return FileStorage.__objects

    def reload(self):
        """Loads storage dictionary from file"""

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """Method for deserializing the JSON file to objects"""
        self.relod()
