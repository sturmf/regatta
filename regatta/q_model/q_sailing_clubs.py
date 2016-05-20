from PyQt5.QtCore import QAbstractListModel, Qt, QModelIndex, QVariant, QObject, pyqtSlot
from regatta import SailingClub
from .q_sailing_club import QSailingClub

class QSailingClubs(QAbstractListModel):
    ObjectRole = Qt.UserRole + 1 # We always want a way to access the underlying object
    NameRole = Qt.UserRole + 2
    _roles = {
        NameRole: "name",
        ObjectRole: "object",
    }

    def __init__(self, q_regatta, parent=None):
        super().__init__(parent)
        self._q_regatta=q_regatta
        self._q_sailing_clubs = {}

    def _roleKey(self, role):
        roles = self.roleNames()
        for key, value in roles.items():
            if value == role:
                return key
        return -1

    def roleNames(self):
        _roles = super().roleNames()
        _roles.update(self._roles)
        return _roles

    @pyqtSlot(result=int)
    @pyqtSlot(QModelIndex, result=int)
    def rowCount(self, parent=QModelIndex()):
        return self._q_regatta._regatta.session.query(SailingClub).count()

    @pyqtSlot(int, result=QSailingClub)
    def get(self, row):
        #index = super().index(row, 0)
        #data = self.data(index, self._roleKey(role))
        data = self._q_regatta._regatta.session.query(SailingClub).order_by(SailingClub.id).all()[row]
        data = self.find_q_sailing_club(data)
        return data

    @pyqtSlot(int, result=QModelIndex)
    @pyqtSlot(int, int, result=QModelIndex)
    @pyqtSlot(int, int, QModelIndex, result=QModelIndex)
    def index(self, row, column=0, parent=QModelIndex()):
        return super().index(row, column, parent)

    @pyqtSlot(QModelIndex, int, result=QVariant)
    def data(self, index, role=Qt.DisplayRole):
        try:
            sailing_club = self._q_regatta._regatta.session.query(SailingClub).order_by(SailingClub.id).all()[index.row()]
            q_sailing_club = self.find_q_sailing_club(sailing_club)
        except IndexError:
            return QVariant()

        if role == self.ObjectRole:
            print("Now return sc", q_sailing_club)
            return q_sailing_club
        elif role == self.NameRole:
            return q_sailing_club.name

        return QVariant()

    def find_q_sailing_club(self, sailing_club):
        q_sailing_club = self._q_sailing_clubs.get(sailing_club.id)
        if not q_sailing_club:
            q_sailing_club = QSailingClub(sailing_club, self)
            self._q_sailing_clubs[sailing_club.id] = q_sailing_club
        return q_sailing_club
