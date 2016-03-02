import datetime
import enum
import os
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Here we create the database base type.
Base = declarative_base()


class Regatta():  # FIXME rename to RegattaModel and file to regatta_model
    """This is the data model of the application, it implements persistence through the SQLAlchemy database."""

    class Mode(enum.Enum):
        Yardstick, Class = range(2)

    def __init__(self, filename='regatta.rgs', overwrite=False):
        if overwrite and os.path.exists(filename):
            os.remove(filename)
        # Create a connection to a new or existing database
        engine = create_engine('sqlite:///' + filename, echo=False)
        db_session = sessionmaker(bind=engine)
        self.session = db_session()
        Base.metadata.create_all(engine)

    """Create the event instance"""
    def new_event(self, name=''):
        event = Event()
        event.name = name
        self.session.add(event)
        return event

    def save(self):
        print('saving changed to database')
        self.session.commit()


class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    """name of the event"""
    name = Column(String, nullable=False)
    """kind of the event either Class or Yardstick"""
    mode = Column(Enum(*[x.name for x in Regatta.Mode], name='mode_types'))
    """first day of the event"""
    start_date = Column(Date)
    """last day of the event"""
    end_date = Column(Date)
    """amount of races scheduled during the event"""
    race_count = Column(Integer)
    """the sailing club that organizes the event"""
    organizer_id = Column(Integer, ForeignKey('sailing_club.id'))
    organizer = relationship("SailingClub")
    """the person responsible for the execution of the event"""
    race_committee_id = Column(Integer, ForeignKey('person.id'))
    race_committee = relationship("Person")

    def __init__(self):
        self.name = ''
        self.mode = Regatta.Mode.Yardstick.name
        self.start_date = datetime.datetime.utcnow()
        self.end_date = datetime.datetime.utcnow()
        self.race_count = 1


class SailingClub(Base):
    __tablename__ = 'sailing_club'

    id = Column(Integer, primary_key=True)
    """full name of the sailing club"""
    name = Column(String, nullable=False, default='')
    """official abbreviation of the sailing club"""
    abbreviation = Column(String, nullable=False, default='')
    """the registration number of the sailing club, if applicable"""
    registration = Column(String, nullable=False, default='')


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False, default='')
    last_name = Column(String, nullable=False, default='')
