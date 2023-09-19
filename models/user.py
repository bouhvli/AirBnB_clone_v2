#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import VARCHAR, Column
from models.base_model import BaseModel
from sqlalchemy.orm import relationship

from models.engine.db_storage import DBStorage

class User(BaseModel):
    """This class defines a user by various attributes"""
    if DBStorage == "db":
        __tablename__ = "users"
        email = Column(VARCHAR(128), nullable=False)
        password = Column(VARCHAR(128), nullable=False)
        first_name = Column(VARCHAR(128), nullable=True)
        last_name = Column(VARCHAR(128), nullable=True)
        places = relationship("Place", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""