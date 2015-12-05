from PyQt5.QtCore import pyqtProperty, pyqtSignal, QObject
from regatta import Regatta


# This is the type that will be registered with QML. It must be a sub-class of QObject.
class QRegatta(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._filename = None
        self._regatta = None

    # All signals
    filenameChanged = pyqtSignal()
    nameChanged = pyqtSignal()
    modusChanged = pyqtSignal()

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
        if self._filename != filename:
            self._filename = filename
            # create a new Regatta instance with the filename
            self._regatta = Regatta(filename)
            print('filename changed to %s' % self._filename)
            # We just created a new Regatta instance, invalidate all properties
            self.filenameChanged.emit()
            self.nameChanged.emit()
            self.modusChanged.emit()

    # The name property

    @pyqtProperty('QString', notify=nameChanged)
    def name(self):
        return self._regatta.name

    @name.setter
    def name(self, name):
        print('name changed to %s' % name)
        if self._regatta.name != name:
            self._regatta.name = name
            self.nameChanged.emit()

    # The modus property

    @pyqtProperty('QString', notify=modusChanged)
    def modus(self):
        return str(self._regatta.modus.value)

    @modus.setter
    def modus(self, modus):
        print('modus changed to %s' % modus)
        if self._regatta.modus.value != int(modus):
            self._regatta.modus = Regatta.Modus(int(modus))
            self.modusChanged.emit()