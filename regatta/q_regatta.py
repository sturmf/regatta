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
    uuidChanged = pyqtSignal()
    nameChanged = pyqtSignal()
    abbreviationChanged = pyqtSignal()
    registrationChanged = pyqtSignal()
    was_organizerChanged = pyqtSignal()

    def sailing_club(self):  # FIXME: maybe rename to inner_model
        return self._sailing_club

    @pyqtProperty('QString', notify=uuidChanged)
    def uuid(self):
        return str(self._sailing_club.uuid) if self._sailing_club else ''

    @pyqtProperty('QString', notify=nameChanged)
    def name(self):
        return self._sailing_club.name if self._sailing_club else 'Not selected'

    @name.setter
    def name(self, name):
        if self._sailing_club.name != name:
            self._sailing_club.name = name
            self.nameChanged.emit()

    @pyqtProperty('QString', notify=abbreviationChanged)
    def abbreviation(self):
        return self._sailing_club.abbreviation if self._sailing_club else ''

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        if self._sailing_club.abbreviation != abbreviation:
            self._sailing_club.abbreviation = abbreviation
            self.abbreviationChanged.emit()

    @pyqtProperty('QString', notify=registrationChanged)
    def registration(self):
        return self._sailing_club.registration if self._sailing_club else ''

    @registration.setter
    def registration(self, registration):
        if self._sailing_club.registration != registration:
            self._sailing_club.registration = registration
            self.registrationChanged.emit()

    @pyqtProperty('bool')
    def was_organizer(self):
        return self._sailing_club.was_organizer

    @was_organizer.setter
    def was_organizer(self, was_organizer):
        if self._sailing_club.was_organizer != was_organizer:
            self._sailing_club.was_organizer = was_organizer
            self.was_organizerChanged.emit()


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

    def __init__(self, q_regatta, event, parent=None):
        QObject.__init__(self, parent)
        self._q_regatta = q_regatta
        self._event = event
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
        return [mode.name for mode in Event.Mode]

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
        return str(Event.Mode[self._event.mode].value)

    @mode.setter
    def mode(self, mode):
        if self._event.mode != Event.Mode(int(mode)).name:
            print('mode changed to %s' % mode)
            self._event.mode = Event.Mode(int(mode)).name
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
        organizer = self._q_regatta.find_q_sailing_club(self._event.organizer)
        print('Found sailing club %s' % organizer)
        return organizer

    @organizer.setter
    def organizer(self, q_organizer):
        if self._event.organizer != q_organizer.sailing_club():
            print('organizer changed to %s' % q_organizer.name)
            self._event.organizer = q_organizer.sailing_club()
            q_organizer.was_organizer = True
            self.organizerChanged.emit()


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
        self._sailing_clubs = [QSailingClub(sailing_club) for sailing_club in self._regatta.session.query(SailingClub).all()]
        # Register for was_organizer changes
        for q_sailing_club in self._sailing_clubs:
            q_sailing_club.was_organizerChanged.connect(self.refresh_organizers)

    @pyqtProperty(QQmlListProperty, notify=eventsChanged)
    def events(self):
        return QQmlListProperty(QEvent, self, self._events)

    @pyqtSlot(str)
    def new_event(self, name):
        event = self._regatta.new_event(name)
        qevent = QEvent(self, event)
        self._events.append(qevent)
        self.eventCreated.emit(qevent)

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

    @pyqtProperty(QQmlListProperty, notify=sailingClubsChanged)
    def sailing_clubs(self):
        return QQmlListProperty(QSailingClub, self, self._sailing_clubs)

    def find_q_sailing_club(self, sailing_club):
        for q_sailing_club in self._sailing_clubs:
            if q_sailing_club.sailing_club() == sailing_club:
                return q_sailing_club
        return None

    def refresh_organizers(self):
        print('organizers refresh')
        self.organizersChanged.emit()

    @pyqtSlot()
    def refresh(self):
        print('refreshing')
        self.organizersChanged.emit()

    @pyqtProperty(QQmlListProperty, notify=organizersChanged)
    def organizers(self):
        print('organizers loaded')
        organizers = [q_sailing_club for q_sailing_club in self._sailing_clubs if q_sailing_club.was_organizer]
        return QQmlListProperty(QSailingClub, self, organizers)

    @pyqtSlot()
    def save(self):
        self._regatta.save()
