import QtQuick 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2
import "components" as Components
import QRegatta 1.0
import QEvent 1.0


ApplicationWindow {

    id: mainWindow
    title: "Regatta program"
    width: 800; height: 600
    color: "gray"
    Accessible.name: "Regatta"

    menuBar: MenuBar {
        Menu {
            title: "&Regatta"
            MenuItem {
                text: "&Open"
                onTriggered: openDialog.visible = true
            }
            MenuItem {
                text: "&Save"
                onTriggered: regattaModel.save()
            }
            MenuItem {
                text: "E&xit"
                shortcut: StandardKey.Quit
                onTriggered: Qt.quit()
            }
        }
    }

    QRegatta {
        id: regattaModel
    }

    Components.Event {
        id: eventView
        anchors.fill: parent
    }

    Components.OpenDialog {
        id: openDialog
        anchors.fill: parent
        signal eventCreated(QEvent event)
        listView.model: regattaModel.events

        onNewEvent: regattaModel.new_event(name) // This delegated the creation to the regatta model
        onEventCreated: eventView.regatta = event // An event was created, so set it as active data model
        onOpenEvent: eventView.regatta = regattaModel.events[index] // An event was selected, so set it as active data model

        Component.onCompleted: { regattaModel.eventCreated.connect(openDialog.eventCreated) }
    }
}
