from .model.regatta import Regatta
from .model.event import Event
from .model.sailing_club import SailingClub
#from .model.person import Person
from .q_model.q_regatta import QRegatta
from .q_model.q_event import QEvent
from .q_model.q_sailing_club import QSailingClub
from .q_model.q_person import QPerson

__all__ = ['Regatta', 'Event', 'SailingClub', 'QRegatta', 'QEvent', 'QSailingClub', 'QPerson']
