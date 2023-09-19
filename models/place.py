#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import VARCHAR, Column, Float, ForeignKey, Integer
from models.base_model import BaseModel
from sqlalchemy.orm import relationship

from models.engine.db_storage import DBStorage


class Place(BaseModel):
    """ A place to stay """
    if DBStorage == "db":
        __tablename__ = "places"
        city_id = Column(VARCHAR(60), ForeignKey("cities.id", "cities_fk"), nullable=False)
        user_id = Column(VARCHAR(60), ForeignKey("users.id", "users_fk"), nullable=False)
        name = Column(VARCHAR(128), nullable=False)
        description = Column(VARCHAR(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0.0
        latitude = 0.0
        longitude = 0.0