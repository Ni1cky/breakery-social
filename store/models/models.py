from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship



Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True, nullable=False)
    hash_password = Column(String)
    name = Column(String)
    surname = Column(String)
    photo = Column(String)
    data = Column(String)
    messages = relationship('Message', backref='user')



class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    time_send = Column(DateTime)
    is_read = Column(Boolean)
    is_important = Column(Boolean)
    is_edited = Column(Boolean)
    author_id = Column(Integer, ForeignKey('user.id'))

