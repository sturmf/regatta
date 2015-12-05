from enum import Enum


class Regatta(object):  # FIXME rename to RegattaModel and file to regatta_model

    class Modus(Enum):
        Yardstick, Class = range(2)

    def __init__(self, filename=''):
        self.filename = filename

        # Load data
        if self.filename:
            self.name = 'Bayerische Jugendwoche'
            self.modus = Regatta.Modus.Yardstick

        else:
            self.name = ''
            self.modus = Regatta.Modus.Class

    def save(self, filename):
        self.filename = filename
