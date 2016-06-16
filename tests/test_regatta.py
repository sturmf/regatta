import datetime
import pytest
from regatta import Regatta, Event


def test_event_defaults():
    filename = 'test.rgs'

    regatta = Regatta(filename, overwrite=True)
    event = regatta.new_event()

    assert(event.name == '')
    assert(event.mode == Event.Mode.Yardstick.name)
    assert(event.start_date == datetime.date.today())
    assert(event.end_date == datetime.date.today())
    assert(event.race_count == 1)
    # FIXME: what should the organizer and race_committee be?


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

    # Test persistence
    regatta.save()

    # reload regatta
    event_id = event.id
    regatta = Regatta(filename)
    event = regatta.session.query(Event).filter(Event.id == event_id).one()
    assert(event.name == name)


def test_organizer_deletion():
    filename = 'test.rgs'

    # Test default value
    regatta = Regatta(filename, overwrite=True)
    event = regatta.new_event()
    sailing_club = regatta.new_sailing_club()
    event.organizer = sailing_club

    # Test persistence
    regatta.save()
    event_id = event.id
    sailing_club_id = sailing_club.id

    # reload regatta
    regatta = Regatta(filename)
    event = regatta.session.query(Event).filter(Event.id == event_id).one()
    print(event.organizer)
    assert(event.organizer.id == sailing_club.id)

    # Test deletion
    regatta.session.delete(event.organizer)
    regatta.save()
   
    # reload regatta
    regatta = Regatta(filename)
    event = regatta.session.query(Event).filter(Event.id == event_id).one()
    print(event.organizer)
    assert(event.organizer == None)
