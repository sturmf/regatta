import pytest
from regatta.regatta import Regatta

def test_regatta_name():
    name = 'Bayerische Jugendwoche'
    regatta = Regatta()
    regatta.name = name
    assert(regatta.name==name)


def test_empty_regatta_name():
    regatta = Regatta()
    assert(regatta.name=='')


def test_regatta_persistency():
    # Create object
    name = 'Bayerische Jugendwoche'
    regatta = Regatta()
    regatta.name = name
    regatta_dbid = regatta.dbid
    regatta = None

    # Load object
    regatta = Regatta(regatta_dbid)
    assert(regatta.name==name)
 

