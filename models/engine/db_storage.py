#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from os import gentenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor method for DBStorage """
        params = {
                'drivername': 'mysql+mysqldb',
                'username': getenv("HBNB_MYSQL_USER",
                'password': getenv("HBNB_MYSQL_PWD",
                'host': getenv("HBNB_MYSQL_HOST"), 
                'database': getenv("HBNB_MYSQL_DB"),
                
        self.__engine= create_engine(URL.create(**params), pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        
        classes = [User, Place, State, City, Amenity, Review]
        cls_all = []
        for i in classes:
            cls_all.extend(self.__session.query(i).all())

        if (cls):
            cls__name = cls.__name__
            cls_all = list(filter(lamba x: x.__class__.__name__ == cls__name , cls_all))
       
        return {f"{i.__class__.__name__}.{i.id}": i for i in cls_all}

    def new(self, obj):
        """Adds new object to DB"""
        self.__session.add(obj)

    def save(self):
        """Saves to bd"""
        self.__session.commit()
        
    def delete(self, obj=None):
        """Deletes a instance"""
        if (obj):
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                            expire_on_commit=False)
        Session = scoped_session(session_factory)
        BDStorage.__session = Session()

