import datetime
import enum
import os
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from urllib.parse import urlparse

# Here we create the database base type.
Base = declarative_base()


class Regatta(Base):  # FIXME rename to RegattaModel and file to regatta_model
    """This is the data model of the application, it implements persistence through the SQLAlchemy database."""
    __tablename__ = 'regatta'

    @classmethod
    def load_or_create_regatta(cls, filename, overwrite=False):
        # Sanity check
        url = urlparse(filename)
        if len(url.path) < 4:  # FIXME: rest after / must be longer
            raise ValueError('Too short database name')

        # Delete already existing database file in overwrite mode
        if overwrite and os.path.exists(url.path):
            os.remove(url.path)

        # Create a connection to a new or existing database
        engine = create_engine('sqlite:///' + url.path, echo=True)
        db_session = sessionmaker(bind=engine)
        cls.session = db_session()
        Base.metadata.create_all(engine)

        # Load or create the regatta instance
        regatta = Regatta.session.query(Regatta).first()
        if not regatta:
            regatta = Regatta()
            regatta.name = os.path.splitext(filename)[0]
            Regatta.session.add(regatta)

            organizer = SailingClub(name='Segel Club Würmsee')
            regatta.organizer = organizer
            Regatta.session.add(organizer)

            race_committee = Person(first_name='Peter', last_name='Parker')
            regatta.race_committee = race_committee
            Regatta.session.add(race_committee)

            Regatta.session.commit()
        return regatta

    class Modus(enum.Enum):
        Yardstick, Class = range(2)

    id = Column(Integer, primary_key=True)
    """name of the event"""
    name = Column(String, nullable=False, default='')
    """kind of the event either Class or Yardstick"""
    modus = Column(Enum(*[x.name for x in Modus], name='modus_types'), default=Modus.Class.name)
    """first day of the event"""
    start_date = Column(Date, default=datetime.datetime.utcnow)
    """last day of the event"""
    end_date = Column(Date, default=datetime.datetime.utcnow)
    """amount of races scheduled during the event"""
    race_count = Column(Integer, default=1)
    """the sailing club that organizes the event"""
    organizer_id = Column(Integer, ForeignKey('sailing_club.id'))
    organizer = relationship("SailingClub")
    """the person responsible for the execution of the event"""
    race_committee_id = Column(Integer, ForeignKey('person.id'))
    race_committee = relationship("Person")

    def __init__(self):
        pass

    @classmethod
    def save(cls):
        Regatta.session.commit()


class SailingClub(Base):
    __tablename__ = 'sailing_club'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default='')
    abbreviation = Column(String, nullable=False, default='')
    registration = Column(String, nullable=False, default='')


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False, default='')
    last_name = Column(String, nullable=False, default='')
