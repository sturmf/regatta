import datetime
import enum
import os
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Here we create the database base type.
BASE = declarative_base()


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
        BASE.metadata.create_all(engine)

    def new_event(self, name=''):
        """Create the event instance"""
        event = Event()
        event.name = name
        self.session.add(event)
        return event

    def new_sailing_club(self, name='Not Set'):
        """Create the sailing_club instance"""
        sailing_club = SailingClub()
        sailing_club.name = name
        self.session.add(sailing_club)
        return sailing_club

    def delete_sailing_club(self, sailing_club):
        if sailing_club in self.session.new:
            self.session.expunge(sailing_club)
        else:
            self.session.delete(sailing_club)

    def save(self):
        print('saving changed to database')
        self.session.commit()


class Event(BASE):
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
        self.start_date = datetime.date.today()
        self.end_date = datetime.date.today()
        self.race_count = 1


class SailingClub(BASE):
    __tablename__ = 'sailing_club'

    id = Column(Integer, primary_key=True)
    """full name of the sailing club"""
    name = Column(String, nullable=False)
    """official abbreviation of the sailing club"""
    abbreviation = Column(String, nullable=False)
    """the registration number of the sailing club, if applicable"""
    registration = Column(String, nullable=False)

    def __init__(self):
        self.name = ''
        self.abbreviation = ''
        self.registration = ''


class Person(BASE):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    def __init__(self):
        self.first_name = ''
        self.last_name = ''
