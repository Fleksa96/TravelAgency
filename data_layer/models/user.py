from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from flask_app import db


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(40), nullable=False, )
    last_name = Column(String(40), nullable=False)
    username = Column(String(20), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    email = Column(String(80), nullable=False, unique=True)
    user_type = Column(Integer, nullable=True, default=3)

    def __init__(self,
                 id=None,
                 first_name=None,
                 last_name=None,
                 username=None,
                 password=None,
                 email=None,
                 user_type=None
                 ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.user_type = user_type
