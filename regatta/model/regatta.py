import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import BASE
from .event import Event
from .sailing_club import SailingClub


class Regatta():  # FIXME rename to RegattaModel and file to regatta_model
    """This is the data model of the application, it implements persistence through the SQLAlchemy database."""

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
        self.session.flush()
        return event

    def new_sailing_club(self, name='Not Set'):
        """Create the sailing_club instance"""
        sailing_club = SailingClub()
        sailing_club.name = name
        self.session.add(sailing_club)
        self.session.flush()
        return sailing_club

    def delete_sailing_club(self, sailing_club):
        if sailing_club in self.session.new:
            self.session.expunge(sailing_club)
        else:
            self.session.delete(sailing_club)

    def save(self):
        print('saving changed to database')
        self.session.commit()
