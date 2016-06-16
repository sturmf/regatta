function editSailingClubs(parent, regatta, event) {
    function sailingClubSelected(sailing_club) {
        event.organizer = sailing_club
    }

    var component = Qt.createComponent("SailingClubs.qml");
    var sailingClubs = component.createObject(parent, {"regatta": regatta, "event": event, "selectedSailingClub": event.organizer});
    sailingClubs.show();
    sailingClubs.sailingClubSelected.connect(sailingClubSelected)
}
