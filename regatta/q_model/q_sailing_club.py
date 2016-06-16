from PyQt5.QtCore import pyqtProperty, pyqtSignal, QObject


# This is the type that will be registered with QML. It must be a sub-class of QObject.
class QSailingClub(QObject):

    def __init__(self, q_regatta, sailing_club, parent=None):
        QObject.__init__(self, parent)
        self._q_regatta = q_regatta
        self._sailing_club = sailing_club
        print("sailing_club constructed")

    def __del__(self):
        print("sc destroyed")
        self._q_regatta._regatta.session.delete(self._sailing_club)

    # All signals
    dataChanged = pyqtSignal()
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
            self.dataChanged.emit()

    @pyqtProperty('QString', notify=abbreviationChanged)
    def abbreviation(self):
        return self._sailing_club.abbreviation if self._sailing_club else ''

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        if self._sailing_club.abbreviation != abbreviation:
            self._sailing_club.abbreviation = abbreviation
            self.abbreviationChanged.emit()
            self.dataChanged.emit()

    @pyqtProperty('QString', notify=registrationChanged)
    def registration(self):
        return self._sailing_club.registration if self._sailing_club else ''

    @registration.setter
    def registration(self, registration):
        if self._sailing_club.registration != registration:
            self._sailing_club.registration = registration
            self.registrationChanged.emit()
            self.dataChanged.emit()

    @pyqtProperty('bool')
    def was_organizer(self):
        return self._sailing_club.was_organizer

    @was_organizer.setter
    def was_organizer(self, was_organizer):
        if self._sailing_club.was_organizer != was_organizer:
            self._sailing_club.was_organizer = was_organizer
            self.was_organizerChanged.emit()
            self.dataChanged.emit()
