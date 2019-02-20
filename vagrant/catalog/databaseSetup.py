import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class User(Base):
    __tablename__ = 'user'
   
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    pwd = Column(String(12), nullable=False)
 
class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    description = Column(String(250))
    category = Column(String(250))
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User) 

#We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):
       
       return {
           'name'       : self.name,
           'description': self.description,
           'id'         : self.id,
           'category'      : self.category
       }
 

engine = create_engine('sqlite:///itemCatalog.db')
 

Base.metadata.create_all(engine)