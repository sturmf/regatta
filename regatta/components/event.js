
function editSailingClubs(parent, regatta, event) {
    function sailingClubSelected(sailing_club) {
        event.organizer = sailing_club
        parent.currentIndex = getIndex(regatta.organizers, sailing_club)
        console.log('New sailing club selected: ' + event.organizer)
    }

    var component = Qt.createComponent("SailingClubs.qml");
    var sailingClubs = component.createObject(parent, {"regatta": regatta, "event": event});
    sailingClubs.show();
    sailingClubs.sailingClubSelected.connect(sailingClubSelected)
}


function getIndex(list, element) {
    if (list && element) {
        console.log('getIndex: ' + list + ', ' + element + ', ' + element.uuid)
        console.log('length: ' + list.length)

        for (var i = 0; i < list.length; i++) {
            if (list[i].uuid === element.uuid) {
                console.log('return:' + i + ', ' + list[i].uuid)
                return i
            }
        }
    }
    console.log('return -1')
    return -1
}
