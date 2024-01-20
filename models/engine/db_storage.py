#!/usr/bin/python3
"""DB storage module for HBNB project"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage instance"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            # Drop all tables if environment is test
            Base.metadata.drop_all(self.__engine)
        
    def all(self, cls=None):
        """Query all objects depending on the class name (cls)"""
        all_classes = {"State": State, "City": City, "User": User,
                       "Place": Place, "Review": Review, "Amenity": Amenity}
        objects = {}
        if cls:
            cls = all_classes[cls] if type(cls) == str else cls
            for obj in self.__session.query(cls).all():
                key = f"{obj.__class__.__name__}.{obj.id}"
                objects[key] = obj
        else:
            for class_name in all_classes:
                cls = all_classes[class_name]
                for obj in self.__session.query(cls).all():
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objects[key] = obj
        return objects 

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload the database session."""
        # Create the engine
        # ... existing engine creation code ...

        # Create all tables in the database
        Base.metadata.create_all(self.__engine)

        # Create the session
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
        
    def close(self):
        """Close the current SQLAlchemy session."""
        self.__session.close()


