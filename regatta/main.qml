import QtQuick 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2
import "main.js" as Main


ApplicationWindow {

    id: mainWindow
    title: "Regatta program"
    width: 800; height: 600
    color: "gray"
    Accessible.name: "Regatta"

    property string filename: ""

    menuBar: MenuBar {
        Menu {
            title: "&Regatta"
            MenuItem {
                text: "&New"
                onTriggered: Main.openFile(true)
            }
            MenuItem {
                text: "&Open"
                onTriggered: fileOpenDialog.visible = true
            }
            MenuItem {
                text: "E&xit"
                shortcut: StandardKey.Quit
                onTriggered: Qt.quit()
            }
            MenuItem {
                text: "&Save"
                onTriggered: pageLoader.item.regatta.save()
            }
        }
    }

    FileDialog {
        id: fileOpenDialog
        title: "Please choose a file"
        onAccepted: Main.openFile(false)
        onRejected: {
            console.log("Canceled")
        }
    }

    Loader {
        anchors.fill: parent
        id: pageLoader
    }

}
