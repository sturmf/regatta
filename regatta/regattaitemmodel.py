import os
from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt, QUrl, QVariant


# FIXME: do we really nees an own class
class Regatta(object):

    def __init__(self, name, url):
        self._name = name
        self._url = url

    def name(self):
        return self._name

    def url(self):
        return self._url


# This is a simple ItemModel to hold all available regattas the user can open.
# Later on we might want to collect more information about the regattas etc.
# The reason for something like this is that we never want the user to have to deal with files.
# On the filesystem we later want to keep the files as:
# regattas/2016/Bayerische Jugendwoche.rgs
class RegattaItemModel(QAbstractListModel):

    NameRole = Qt.UserRole + 1
    UrlRole = Qt.UserRole + 2

    _roles = {NameRole: "name", UrlRole: "url"}

    def __init__(self, parent=None):
        super(RegattaItemModel, self).__init__(parent)
        # Find all files ending in ".rgs" and create Regatta objects out of them
        self._regattas = [Regatta(os.path.splitext(os.path.basename(f))[0], f) for f in os.listdir('.') if f.endswith('.rgs')]

    # FIXME: unused, keep it for now
    def addRegatta(self, regatta):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._regattas.append(regatta)
        self.endInsertRows()

    def rowCount(self, parent=QModelIndex()):
        return len(self._regattas)

    def data(self, index, role=Qt.DisplayRole):
        try:
            regatta = self._regattas[index.row()]
        except IndexError:
            return QVariant()

        if role == self.NameRole:
            return regatta.name()

        if role == self.UrlRole:
            return regatta.url()

        return QVariant()

    def roleNames(self):
        return self._roles



