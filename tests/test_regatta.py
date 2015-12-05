import pytest
from regatta import Regatta

# FIXME: this is open for discussion, I put more tests in a single unit test, since they all need the same setup
def test_regatta_name():
    name = 'Bayerische Jugendwoche'

    # Test default value
    regatta = Regatta()
    assert(regatta.name == '')

    # Test value acceptance
    regatta.name = name
    assert(regatta.name==name)

    # Test persistency
    filename = 'test.reg'
    regatta.save(filename)
    regatta = None
    # reload regatta
    regatta = Regatta(filename)
    assert(regatta.name == name)
