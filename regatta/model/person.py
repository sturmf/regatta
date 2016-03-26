from sqlalchemy import Column, Integer, String
from .base import BASE


class Person(BASE):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    def __init__(self):
        self.first_name = ''
        self.last_name = ''
