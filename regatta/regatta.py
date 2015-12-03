
class Regatta(object): # FIXME rename to RegattaModel and file to regatta_model

    def __init__(self, dbid=None):
        self.dbid = 1
        if dbid:
            self.name = 'Bayerische Jugendwoche'
        else:
            self.name = ''

#    @property
#    def name(self):
#        return self._name

#    @name.setter
#    def name(self, name):
#        self._name = str(name)
