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

    // This is the base model instance
    QRegatta {
        id: regattaModel
    }

    // This is a factory that allows to create the eventView on demand
    // We can only create it after we have the proper event model
    Component {
        id: eventFactory

        Components.Event {
            id: eventView
            anchors.fill: parent
        }
     }

    // This is a placeholder which will be the parent of the eventView
    Item {
        id: eventViewItem
        anchors.fill: parent
    }

    Components.OpenDialog {
        id: openDialog
        anchors.fill: parent
        signal eventCreated(QEvent event)
        listView.model: regattaModel.events

        onNewEvent: regattaModel.new_event(name) // This delegated the creation to the regatta model
        onEventCreated: eventFactory.createObject(eventViewItem, {event: event}) // An event was created, so set it as active data model
        onOpenEvent: eventFactory.createObject(eventViewItem, {event: regattaModel.events[index]}) // An event was selected, so set it as active data model
        Component.onCompleted: { regattaModel.eventCreated.connect(openDialog.eventCreated) }
    }
}
