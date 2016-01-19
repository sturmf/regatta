import enum
import os
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import urlparse

# Here we create the database base type.
Base = declarative_base()


class Regatta(Base):  # FIXME rename to RegattaModel and file to regatta_model
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
            Regatta.session.add(regatta)
            Regatta.session.commit()
        return regatta

    class Modus(enum.Enum):
        Yardstick, Class = range(2)

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default='')
    modus = Column(Enum(*[x.name for x in Modus], name='modus_types'), default=Modus.Class.name)

    def __init__(self):
        pass

    @classmethod
    def save(cls):
        Regatta.session.commit()
