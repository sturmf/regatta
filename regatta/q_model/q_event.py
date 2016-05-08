from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot, QObject
from regatta import Event
from .q_sailing_club import QSailingClub

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

