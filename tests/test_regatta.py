import pytest
from regatta import Regatta

# FIXME: this is open for discussion, I put more tests in a single unit test, since they all need the same setup
def test_regatta_name():
    filename = 'test.reg'
    name = 'Bayerische Jugendwoche'
    # FIXME: add mode, start_date

    # Test default value
    regatta = Regatta.load_or_create_regatta(filename, overwrite=True)
    assert(regatta.name == 'test')

    # Test value acceptance
    regatta.name = name
    assert(regatta.name == name)

    # Test persistency
    regatta.save()

    # reload regatta
    regatta = Regatta.load_or_create_regatta(filename)
    assert(regatta.name == name)
