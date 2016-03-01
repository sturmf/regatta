import pytest
from regatta import Regatta, Event


# FIXME: this is open for discussion, I put more tests in a single unit test, since they all need the same setup
def test_regatta_name():
    filename = 'test.rgs'
    name = 'Bayerische Jugendwoche'
    # FIXME: add mode, start_date

    # Test default value
    regatta = Regatta(filename, overwrite=True)
    event = regatta.new_event()

    # Test value acceptance
    event.name = name
    assert(event.name == name)

    # Test persistency
    regatta.save()

    # reload regatta
    event_id = event.id
    regatta = Regatta(filename)
    event = regatta.session.query(Event).filter(Event.id == event_id).one()
    assert(event.name == name)
