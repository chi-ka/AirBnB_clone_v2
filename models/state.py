#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if models.storage_t == 'db':
        # If using database storage
        cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")
    else:
        # If using file storage
        @property
        def cities(self):
            """Returns the list of City instances with state_id equals to the current State.id"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

