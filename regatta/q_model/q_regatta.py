from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot, QObject, QAbstractListModel
from PyQt5.QtQml import QQmlListProperty
from regatta import Regatta, Event, SailingClub
from .q_event import QEvent
from .q_sailing_club import QSailingClub
from .q_sailing_clubs import QSailingClubs


# This is the type that will be registered with QML. It must be a sub-class of QObject.
class QRegatta(QObject):

    # All signals
    eventCreated = pyqtSignal(QEvent)
    sailingClubCreated = pyqtSignal(QSailingClub)
    eventsChanged = pyqtSignal()
    sailingClubsChanged = pyqtSignal()
    organizersChanged = pyqtSignal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        # Load the model that we adapt
        self._regatta = Regatta()
        self._events = [QEvent(self, event) for event in self._regatta.session.query(Event).all()]
        self._q_sailing_clubs = QSailingClubs(self, parent)
        # Register for was_organizer changes
        #for q_sailing_club in self._sailing_clubs:
        #    q_sailing_club.was_organizerChanged.connect(self.refresh_organizers)

    @pyqtProperty(QQmlListProperty, notify=eventsChanged)
    def events(self):
        return QQmlListProperty(QEvent, self, self._events)

    @pyqtSlot(str)
    def new_event(self, name):
        event = self._regatta.new_event(name)
        qevent = QEvent(self, event)
        self._events.append(qevent)
        self.eventCreated.emit(qevent)
        self.eventsChanged.emit()

    @pyqtSlot()
    def new_sailing_club(self):
        sailing_club = self._regatta.new_sailing_club()
        q_sailing_club = QSailingClub(sailing_club)
        q_sailing_club.was_organizerChanged.connect(self.refresh_organizers)
        self._sailing_clubs.append(q_sailing_club)
        self.sailingClubsChanged.emit()
        self.sailingClubCreated.emit(q_sailing_club)

    @pyqtSlot(QSailingClub)
    def delete_sailing_club(self, sailing_club):
        if sailing_club:
            self._sailing_clubs.remove(sailing_club)
            self._regatta.delete_sailing_club(sailing_club.sailing_club())
            self.sailingClubsChanged.emit()

    @pyqtProperty(QSailingClubs, notify=sailingClubsChanged)
    def sailing_clubs(self):
        return self._q_sailing_clubs

    def refresh_organizers(self):
        print('organizers refresh')
        self.organizersChanged.emit()

    @pyqtSlot()
    def refresh(self):
        print('refreshing')
        self.organizersChanged.emit()

    @pyqtProperty(QSailingClubs, notify=sailingClubsChanged)
    def organizers(self):
        # FIXME: return a QSortFilterProxyModel
        return self._q_sailing_clubs

    @pyqtSlot()
    def save(self):
        self._regatta.save()
