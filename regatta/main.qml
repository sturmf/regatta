import QtQuick 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2
import "main.js" as Main
import "OpenDialog"
import RegattaItemModel 1.0

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
                onTriggered: openDialog.visible = true
            }
            MenuItem {
                text: "&Save"
                onTriggered: pageLoader.item.regatta.save()
            }
            MenuItem {
                text: "E&xit"
                shortcut: StandardKey.Quit
                onTriggered: Qt.quit()
            }
        }
    }

    Loader {
        anchors.fill: parent
        id: pageLoader
    }

    OpenDialog {
        id: openDialog
        anchors.fill: parent
        onNewRegatta: Main.newRegatta(name)
        onOpenRegatta: Main.openRegatta(url)
        listView.model: RegattaItemModel {}
    }

}
