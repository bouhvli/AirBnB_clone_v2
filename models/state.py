#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import dbStorage, FileStorage
from models.city import City

class State(BaseModel, Base):
    """ State class """
    if dbStorage == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""
        cities = {}
        
        @property
        def cities(self):
            cities = FileStorage.all("cities")
            cities_by_state = {k: v for k,v in cities.items() if v["state_id"] == self.id}
            return cities_by_state
