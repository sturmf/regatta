/* This is a small helper that calculates the position of an element in a list */
function getIndex(list, element) {
    if (list && element) {
        for (var i = 0; i < list.rowCount(); i++) {
            if (list.get(i).uuid === element.uuid) {
                return i
            }
        }
    }
    return -1
}
