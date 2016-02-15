from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot, QObject
from regatta import Regatta


# This is the type that will be registered with QML. It must be a sub-class of QObject.
class QRegatta(QObject):

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self._filename = None
        self._regatta = None
        print("constructed")

    # All signals
    filenameChanged = pyqtSignal()
    nameChanged = pyqtSignal()
    modusChanged = pyqtSignal()
    startDateChanged = pyqtSignal()
    endDateChanged = pyqtSignal()

    # The modes static list

    @pyqtProperty('QStringList', constant=True)
    def modes(self):
        return [modus.name for modus in Regatta.Modus]

    # The file_name property

    @pyqtProperty('QString', notify=filenameChanged)
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        if filename and self._filename != filename:
            print('filename changed to %s' % filename)
            self._filename = filename
            # create a new Regatta instance with the filename
            self._regatta = Regatta.load_or_create_regatta(self._filename)
            # We just created a new Regatta instance, invalidate all properties

    # The name property

    @pyqtProperty('QString', notify=nameChanged)
    def name(self):
        return self._regatta.name

    @name.setter
    def name(self, name):
        if self._regatta.name != name:
            print('name changed to %s' % name)
            self._regatta.name = name
            self.nameChanged.emit()

    # The modus property

    @pyqtProperty('QString', notify=modusChanged)
    def modus(self):
        return str(Regatta.Modus[self._regatta.modus].value)

    @modus.setter
    def modus(self, modus):
        if self._regatta.modus != Regatta.Modus(int(modus)).name:
            print('modus changed to %s' % modus)
            self._regatta.modus = Regatta.Modus(int(modus)).name
            self.modusChanged.emit()

    # The start_date property

    @pyqtProperty('QDate', notify=startDateChanged)
    def start_date(self):
        return self._regatta.start_date

    @start_date.setter
    def start_date(self, start_date):
        if self._regatta.start_date != start_date.toPyDate():
            print('start_date changed to %s' % start_date)
            self._regatta.start_date = start_date.toPyDate()
            self.startDateChanged.emit()

    # The end_date property

    @pyqtProperty('QDate', notify=endDateChanged)
    def end_date(self):
        return self._regatta.end_date

    @end_date.setter
    def end_date(self, end_date):
        if self._regatta.end_date != end_date.toPyDate():
            print('end_date changed to %s' % end_date)
            self._regatta.end_date = end_date.toPyDate()
            self.endDateChanged.emit()

    @pyqtSlot()
    def save(self):
        self._regatta.save()
