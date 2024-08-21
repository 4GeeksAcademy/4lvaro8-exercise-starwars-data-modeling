import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, unique=True, primary_key=True)
    username = Column(String(20), nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(200), unique=True, nullable=False)

    
    def serialize(self):
        return {
            "user_id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }



class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name= Column(String(80), nullable=False)
    description= Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    climate = Column(String(80), nullable=False)
    terrain = Column(String(80), nullable=False)


    def serialize(self):
        return {
            "planet_id": self.id,
            "planet_name": self.name,
            "description": self.description,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "climate": self.climate,
            "terrain": self.terrain
        }
    


class Characters(Base):
    __tablename__ = 'characters'

    id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(60), nullable=False)
    description = Column(String(250), nullable=False)
    gender = Column(String(60), nullable=False)
    mass = Column(Integer, nullable=False)


    def serialize(self):
        return {
            "Character_id": self.id,
            "name": self.name,
            "description": self.description,
            "gender": self.gender,
            "mass": self.mass
        }
    


class Favorites(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    character_id = Column(Integer, ForeignKey(Characters.id), nullable=False)
    planet_id = Column(Integer, ForeignKey(Planets.id), nullable=False)


    def serialize(self):
        return {
            "favorite_id": self.id,
            "user_id": self.user_id,
            "character_name": self.character_id,
            "planet_name": self.planet_id
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
