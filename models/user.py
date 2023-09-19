#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import VARCHAR, Column
from models.base_model import BaseModel
from sqlalchemy.orm import relationship

class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column('email', VARCHAR(128), nullable=False)
    password = Column('password', VARCHAR(128), nullable=False)
    first_name = Column('first_name', VARCHAR(128), nullable=True)
    last_name = Column('last_name', VARCHAR(128), nullable=True)
    places = relationship("Place", backref="Place.user_id", primaryjoin="User.id==Place.user_id")
