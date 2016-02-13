import QtQuick 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.2
import "DatePicker"

TabView {
    id: tabView

    property var regatta

    Tab {
        anchors.rightMargin: 5
        anchors.leftMargin: 5
        anchors.bottomMargin: 5
        anchors.topMargin: 5
        title: "Regatta"

        GridLayout {
            id: gridLayout
            rows: 3
            flow: GridLayout.TopToBottom
            anchors.fill: parent

            Label { text: "Title" }
            Label { text: "Modus" }
            Label { text: "Date" }

            TextField {
                text: regatta.name
                onEditingFinished: regatta.name = text
            }
            ComboBox {
                model: regatta.modes
                currentIndex: regatta.modus
                onCurrentIndexChanged: regatta.modus = currentIndex
            }
            DatePicker {
            }

        }
    }

    Tab {
        title: "Participants"
    }

}



