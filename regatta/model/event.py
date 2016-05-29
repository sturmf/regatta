import datetime
import enum
from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey
from sqlalchemy.orm import relationship, backref
from .base import BASE
from .person import Person


class Event(BASE):
    __tablename__ = 'event'

    class Mode(enum.Enum):
        Yardstick, Class = range(2)

    id = Column(Integer, primary_key=True)
    """name of the event"""
    name = Column(String, nullable=False)
    """kind of the event either Class or Yardstick"""
    mode = Column(Enum(*[x.name for x in Mode], name='mode_types'))
    """first day of the event"""
    start_date = Column(Date)
    """last day of the event"""
    end_date = Column(Date)
    """amount of races scheduled during the event"""
    race_count = Column(Integer)
    """the sailing club that organizes the event"""
    organizer_id = Column(Integer, ForeignKey('sailing_club.id'), nullable=True)
    organizer = relationship("SailingClub", backref=backref('events'))
    """the person responsible for the execution of the event"""
    race_committee_id = Column(Integer, ForeignKey('person.id'), nullable=True)
    race_committee = relationship(Person, backref=backref('events'))

    def __init__(self):
        self.name = ''
        self.mode = Event.Mode.Yardstick.name
        self.start_date = datetime.date.today()
        self.end_date = datetime.date.today()
        self.race_count = 1
