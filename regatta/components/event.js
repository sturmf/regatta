
function editSailingClubs(parent, regatta, event) {
    function sailingClubSelected(sailing_club) {
        event.organizer = sailing_club
        parent.currentIndex = getIndex(regatta.organizers, sailing_club)
    }

    var component = Qt.createComponent("SailingClubs.qml");
    var sailingClubs = component.createObject(parent, {"regatta": regatta, "event": event});
    sailingClubs.show();
    sailingClubs.sailingClubSelected.connect(sailingClubSelected)
}


function getIndex(list, element) {
    if (list && element) {
        for (var i = 0; i < list.length; i++) {
            if (list[i].uuid === element.uuid) {
                return i
            }
        }
    }
    return -1
}
