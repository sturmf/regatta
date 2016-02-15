import QtQuick 2.2
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.1
import QtQuick.Window 2.1

Item {
    height: dateField.height

    property date selectedDate : new Date()
    property string selectedDateFormat: "dd.MM.yyyy"
    property Window activeWindow
    property var pos : getOffset(dateField)

    signal dateChanged (date date)

    TextField {
        id: dateField
        width: parent.width
        readOnly: true
        text: selectedDate.toLocaleDateString(Qt.locale(), selectedDateFormat)
        MouseArea {
            anchors.fill: parent
            onClicked:{ toggleModal() }
        }
    }

    function getOffset(item) {
        var offset = {
            "x": /*activeWindow.x + */item.x,
            "y": /*activeWindow.y + */item.y + item.height
        };
        while(item.parent) {
            item = item.parent;
            offset.x += item.x;
            offset.y += item.y;
        }
        console.debug("total", "x", offset.x, "y", offset.y)

        return offset;
    }

    function toggleModal() {
        if(modal.active) {
            console.log("hide calendar")
            loseFocus();
        }
        else {
            console.log("show calendar")
            calendar.selectedDate = selectedDate
            modal.show()
            modal.requestActivate()
            calendar.focus = true
            calendar.enabled=true
        }
    }

    function loseFocus(newDate) {
        if (newDate instanceof Date) {
            selectedDate = newDate;
            calendar.selectedDate = selectedDate;
            dateChanged(newDate);
        }
        else {
            calendar.selectedDate.setDate(selectedDate.getDate());
        }
        modal.close();
        dateField.focus = true
    }

    Window {
        id: modal
        flags: Qt.Widget //| Qt.ToolTip | Qt.FramelessWindowHint
        minimumHeight: calendar.height; minimumWidth: calendar.width
        maximumHeight: calendar.height; maximumWidth: calendar.width
        x: pos.x
        y: pos.y

        Calendar {
            id: calendar
            width: 200
            height: 300
            onClicked: loseFocus(calendar.selectedDate)
            Keys.onEnterPressed: {
                console.log("enter")
                loseFocus(calendar.selectedDate)
            }
            Keys.onEscapePressed: loseFocus()

        }

    }
}
