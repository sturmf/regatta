from PyQt5.QtCore import QAbstractListModel, Qt, QModelIndex, QVariant, QObject, pyqtSlot
from regatta import SailingClub
from .q_sailing_club import QSailingClub

class QSailingClubs(QAbstractListModel):
    NameRole = Qt.UserRole + 1
    _roles = {
        NameRole: "name",
    }

    def __init__(self, q_regatta, parent=None):
        super().__init__(parent)
        self._q_regatta=q_regatta
        self._q_sailing_clubs = {}

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
        data = self._q_regatta._regatta.session.query(SailingClub).order_by(SailingClub.id).all()[row]
        data = self.resolve(data)
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
            q_sailing_club = self.resolve(sailing_club)
        except IndexError:
            return QVariant()

        if role == self.NameRole or role == Qt.DisplayRole:
            return q_sailing_club.name

        return QVariant()

    def resolve(self, sailing_club):
        q_sailing_club = self._q_sailing_clubs.get(sailing_club.id)
        if not q_sailing_club:
            q_sailing_club = QSailingClub(sailing_club, self)
            q_sailing_club.dataChanged.connect(self._refresh)
            self._q_sailing_clubs[sailing_club.id] = q_sailing_club
        return q_sailing_club

    def _refresh(self):
        # FIXME: use correct index
        self.dataChanged.emit(self.index(0), self.index(0))