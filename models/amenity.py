#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):  #don't forget to add Base to the function Amenity(BaseModel, Base) 
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary='place_amenity', back_populates="amenities")