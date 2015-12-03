from enum import Enum
from PyQt5.QtCore import pyqtProperty, pyqtSignal, QObject


# This is the type that will be registered with QML. It must be a sub-class of QObject.
class QRegatta(QObject):

    class Modus(Enum):
        Yardstick, Class = range(2)

    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialise the value of the properties.
        self._name = 'test2'
        self._modus = QRegatta.Modus.Yardstick

    # All signals
    nameChanged = pyqtSignal()
    modusChanged = pyqtSignal()

    @pyqtProperty('QStringList', constant=True)
    def modes(self):
        return [modus.name for modus in QRegatta.Modus]

    # The name property

    @pyqtProperty('QString', notify=nameChanged)
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        print('name changed to %s' % name)
        if self._name != name:
            self._name = name
            self.nameChanged.emit()

    # The modus property

    @pyqtProperty('QString', notify=modusChanged)
    def modus(self):
        return str(self._modus.value)

    @modus.setter
    def modus(self, modus):
        print('modus changed to %s' % modus)
        if self._modus.value != int(modus):
            self._modus = QRegatta.Modus(int(modus))
            self.modusChanged.emit()
