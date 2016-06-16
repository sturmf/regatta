import uuid
from .guid import GUID
from sqlalchemy import Column, Integer, String, Boolean
from .base import BASE


class SailingClub(BASE):
    __tablename__ = 'sailing_club'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True)
    """a unique id independent of database save"""
    uuid = Column(GUID, nullable=False)
    """full name of the sailing club"""
    name = Column(String, nullable=False)
    """official abbreviation of the sailing club"""
    abbreviation = Column(String, nullable=False)
    """the registration number of the sailing club, if applicable"""
    registration = Column(String, nullable=False)
    """if this sailing club has ever been an organizer"""
    was_organizer = Column(Boolean, nullable=False)

    def __init__(self):
        self.uuid = uuid.uuid4()
        self.name = ''
        self.abbreviation = ''
        self.registration = ''
        self.was_organizer = False
