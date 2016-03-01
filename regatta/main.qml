import QtQuick 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2
import "OpenDialog"
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

    Item {
        id: item
        // This is a hack to capture the Regatta event parameter
        signal eventCreated(QEvent event)
        onEventCreated: {
            console.log(event.name)
            pageLoader.setSource("regatta.qml", {regatta: event})
        }

        QRegatta {
            id: regattaModel
            Component.onCompleted: { regattaModel.eventCreated.connect(item.eventCreated) }
        }
    }

    Loader {
        anchors.fill: parent
        id: pageLoader
    }

    OpenDialog {
        id: openDialog
        anchors.fill: parent
        onNewEvent: regattaModel.new_event(name)
        onOpenEvent: {
            pageLoader.setSource("regatta.qml", {regatta: regattaModel.events[index]})
        }
        listView.model: regattaModel.events
    }
}
