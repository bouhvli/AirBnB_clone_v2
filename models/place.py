#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import VARCHAR, Column, Float, ForeignKey, Integer
from models.base_model import BaseModel
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column("city_id", VARCHAR(60), ForeignKey("cities.id", "cities_fk"), nullable=False)
    user_id = Column("city_id", VARCHAR(60), ForeignKey("users.id", "users_fk"), nullable=False)
    name = Column("name", VARCHAR(128), nullable=False)
    description = Column("description", VARCHAR(1024), nullable=True)
    number_rooms = Column("number_rooms", Integer(), nullable=False, default=0)
    number_bathrooms = Column("number_bathrooms", Integer(), nullable=False, default=0)
    max_guest = Column("max_guest", Integer(), nullable=False, default=0)
    price_by_night = Column("price_by_night", Integer(), nullable=False, default=0)
    latitude = Column("latitude", Float(), nullable=True)
    longitude = Column("longitude", Float(), nullable=True)
    user = relationship("User", foreign_keys="Place.user_id")
    amenity_ids = []
