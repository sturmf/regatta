from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot, QObject


# This is the type that will be registered with QML. It must be a sub-class of QObject.
class QPerson(QObject):

    def __init__(self, person, parent=None):
        QObject.__init__(self, parent)
        self._id = None
        print("person constructed")

    @pyqtProperty('QString')
    def first_name(self):
        return "person works"

