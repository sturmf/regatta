import QtQuick 2.0
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.2


TabView {
    id: tabView

    property var regatta

    Tab {
        title: "Regatta"

        GridLayout {
            id: gridLayout
            rows: 2
            flow: GridLayout.TopToBottom
            anchors.fill: parent

            Label { text: "Title" }
            Label { text: "Modus" }

            TextField {
                text: regatta.name
                onEditingFinished: regatta.name = text
            }
            ComboBox {
                model: regatta.modes
                currentIndex: regatta.modus
                onCurrentIndexChanged: regatta.modus = currentIndex
            }
        }
    }

    Tab {
        title: "Participants"
    }

}

