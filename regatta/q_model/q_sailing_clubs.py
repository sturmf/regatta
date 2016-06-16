from PyQt5.QtCore import QAbstractListModel, Qt, QModelIndex, QVariant, pyqtSlot
from regatta import SailingClub
from .q_sailing_club import QSailingClub


class QSailingClubs(QAbstractListModel):
    NameRole = Qt.UserRole + 1
    _roles = {
        NameRole: b"name",
    }

    def __init__(self, q_regatta, parent=None):
        super().__init__(parent)
        self._q_regatta = q_regatta
        # Load all SailingClubs and create a lookup dict
        self._q_sailing_clubs_list = [QSailingClub(q_regatta, sailing_club, self) for sailing_club in self._q_regatta._regatta.session.query(SailingClub).all()]
        self._q_sailing_clubs_by_uuid = {sailing_club.uuid: sailing_club for sailing_club in self._q_sailing_clubs_list}
        # We need to know when a SailingClub is modified so that we can emit a dataChanged signal
        for q_sailing_club in self._q_sailing_clubs_list:
            q_sailing_club.dataChanged.connect(self._dataChanged)

    def roleNames(self):
        _roles = super().roleNames()
        _roles.update(self._roles)
        return _roles

    @pyqtSlot(result=int)
    @pyqtSlot(QModelIndex, result=int)
    def rowCount(self, parent=QModelIndex()):
        return len(self._q_sailing_clubs_list)

    @pyqtSlot(int, result=QSailingClub)
    def get(self, row):
        return self._q_sailing_clubs_list[row]

    @pyqtSlot(int, result=QModelIndex)
    @pyqtSlot(int, int, result=QModelIndex)
    @pyqtSlot(int, int, QModelIndex, result=QModelIndex)
    def index(self, row, column=0, parent=QModelIndex()):
        return super().index(row, column, parent)

    @pyqtSlot()
    def new_sailing_club(self):
        super().beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        sailing_club = self._q_regatta._regatta.new_sailing_club()
        q_sailing_club = QSailingClub(self._q_regatta, sailing_club, self)
        self._q_sailing_clubs_list.append(q_sailing_club)
        self._q_sailing_clubs_by_uuid[q_sailing_club.uuid] = q_sailing_club
        q_sailing_club.dataChanged.connect(self._dataChanged)
        super().endInsertRows()

    @pyqtSlot(QSailingClub)
    def delete_sailing_club(self, q_sailing_club):
        try:
            # Not very fast, could be indexed if ever necessary
            row = self._q_sailing_clubs_list.index(q_sailing_club)
            super().beginRemoveRows(QModelIndex(), row, row)
            self._q_regatta._regatta.delete_sailing_club(q_sailing_club.sailing_club())
            self._q_sailing_clubs_list.remove(q_sailing_club)
            del self._q_sailing_clubs_by_uuid[q_sailing_club.uuid]
            print("Deleting:", q_sailing_club)
            q_sailing_club.deleteLater()
            super().endRemoveRows()
        except ValueError:
            print("Could not find SailingClub to delete")

    @pyqtSlot(QModelIndex, int, result=QVariant)
    def data(self, index, role=Qt.DisplayRole):
        print("Index:", index.row())
        try:
            q_sailing_club = self._q_sailing_clubs_list[index.row()]
        except IndexError:
            return QVariant()

        if role == self.NameRole or role == Qt.DisplayRole:
            return q_sailing_club.name
        return QVariant()

    def resolve(self, sailing_club):
        if sailing_club:
            return self._q_sailing_clubs_by_uuid.get(str(sailing_club.uuid))
        return None

    def _dataChanged(self):
        try:
            # Not very fast, could be indexed if ever necessary
            row = self._q_sailing_clubs_list.index(self.sender())
            self.dataChanged.emit(self.index(row), self.index(row))
        except ValueError:
            print("Could not find changed SailingClub")
