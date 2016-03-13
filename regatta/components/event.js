
function editSailingClubs(parent, regatta, event) {
    var component = Qt.createComponent("SailingClubs.qml");
    var sailingClubs = component.createObject(parent, {"regatta": regatta, "event": event});
    sailingClubs.show();
}
