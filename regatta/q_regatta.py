from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot, QObject
from PyQt5.QtQml import QQmlListProperty
from regatta import Regatta, Event, SailingClub


# This is the type that will be registered with QML. It must be a sub-class of QObject.
class QSailingClub(QObject):

    def __init__(self, sailing_club, parent=None):
        QObject.__init__(self, parent)
        self._sailing_club = sailing_club
        print("sailing_club constructed")

    # All signals
    nameChanged = pyqtSignal()

    @pyqtProperty('QString', notify=nameChanged)
    def name(self):
        return self._sailing_club.name


# This is the type that will be registered with QML. It must be a sub-class of QObject.
class QPerson(QObject):

    def __init__(self, person, parent=None):
        QObject.__init__(self, parent)
        self._id = None
        print("person constructed")

    @pyqtProperty('QString')
    def first_name(self):
        return "person works"


# This is the type that will be registered with QML. It must be a sub-class of QObject.
class QEvent(QObject):

    def __init__(self, event, parent=None):
        QObject.__init__(self, parent)
        self._event = event
        self._organizer = None
        self._race_committee = None
        print("constructed")

    # All signals
    nameChanged = pyqtSignal()
    modeChanged = pyqtSignal()
    startDateChanged = pyqtSignal()
    endDateChanged = pyqtSignal()
    raceCountChanged = pyqtSignal()
    organizerChanged = pyqtSignal()
    raceCommitteeChanged = pyqtSignal()

    # The modes static list

    @pyqtProperty('QStringList', constant=True)
    def modes(self):
        return [mode.name for mode in Regatta.Mode]

    # The name property

    @pyqtProperty('QString', notify=nameChanged)
    def name(self):
        return self._event.name

    @name.setter
    def name(self, name):
        if self._event.name != name:
            print('name changed to %s' % name)
            self._event.name = name
            self.nameChanged.emit()

    # The mode property

    @pyqtProperty('QString', notify=modeChanged)
    def mode(self):
        return str(Regatta.Mode[self._event.mode].value)

    @mode.setter
    def mode(self, mode):
        if self._event.mode != Regatta.Mode(int(mode)).name:
            print('mode changed to %s' % mode)
            self._event.mode = Regatta.Mode(int(mode)).name
            self.modeChanged.emit()

    # The start_date property

    @pyqtProperty('QDate', notify=startDateChanged)
    def start_date(self):
        return self._event.start_date

    @start_date.setter
    def start_date(self, start_date):
        if self._event.start_date != start_date.toPyDate():
            print('start_date changed to %s' % start_date)
            self._event.start_date = start_date.toPyDate()
            self.startDateChanged.emit()

    # The end_date property

    @pyqtProperty('QDate', notify=endDateChanged)
    def end_date(self):
        return self._event.end_date

    @end_date.setter
    def end_date(self, end_date):
        if self._event.end_date != end_date.toPyDate():
            print('end_date changed to %s' % end_date)
            self._event.end_date = end_date.toPyDate()
            self.endDateChanged.emit()

    # The race_count property

    @pyqtProperty('int', notify=raceCountChanged)
    def race_count(self):
        return self._event.race_count

    @race_count.setter
    def race_count(self, race_count):
        if self._event.race_count != race_count:
            print('race_count changed to %s' % race_count)
            self._event.race_count = race_count
            self.raceCountChanged.emit()

    # The organizer property

    @pyqtProperty(QSailingClub, notify=organizerChanged)
    def organizer(self):
        return self._organizer
        # return self._regatta.organizer


class QRegatta(QObject):

    # All signals
    eventCreated = pyqtSignal(QEvent)
    eventsChanged = pyqtSignal()
    sailingClubsChanged = pyqtSignal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        # Load the model that we adapt
        self._regatta = Regatta()
        self._events = [QEvent(event) for event in self._regatta.session.query(Event).all()]
        self._sailing_clubs = [QSailingClub(sailing_club) for sailing_club in self._regatta.session.query(SailingClub).all()]

    @pyqtProperty(QQmlListProperty, notify=eventsChanged)
    def events(self):
        return QQmlListProperty(QEvent, self, self._events)

    @pyqtSlot(str)
    def new_event(self, name):
        event = self._regatta.new_event(name)
        qevent = QEvent(event)
        self._events.append(qevent)
        self.eventCreated.emit(qevent)

    @pyqtProperty(QQmlListProperty, notify=sailingClubsChanged)
    def sailing_clubs(self):
        return QQmlListProperty(QSailingClub, self, self._sailing_clubs)

    @pyqtSlot()
    def save(self):
        self._regatta.save()
