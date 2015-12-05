import QtQuick 2.0
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.2

import QRegatta 1.0


TabView {
    id: tabView

    property string filename: ""

    anchors.fill: parent
    /*
    anchors.margins: UI.margin
    tabPosition: UI.tabPosition
    */

    // This is our python QRegatta object
    // connect it's inner filename property with the TabView filename
    QRegatta {
        id: regatta
        filename: tabView.filename
    }

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
