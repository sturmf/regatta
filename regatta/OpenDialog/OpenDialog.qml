import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Layouts 1.0


Rectangle {
    id: root
    width: 800
    height: 600

    signal newRegatta(string name)
    signal openRegatta(string url)

    property alias listView: listView

    Button {
        id: newButton
        text: qsTr("New")
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20
        anchors.right: parent.right
        anchors.rightMargin: 20
        onClicked: {
            root.visible = false
            newRegatta(name.text)
        }
    }
    
    TextField {
        id: name
        anchors.right: newButton.left
        anchors.rightMargin: 10
        anchors.left: parent.left
        anchors.leftMargin: 20
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20
        placeholderText: qsTr("Regatta Name")
    }
    
    ListView {
        id: listView
        contentHeight: 0
        anchors.bottom: name.top
        anchors.right: parent.right
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottomMargin: 20
        anchors.rightMargin: 20
        anchors.leftMargin: 20
        anchors.topMargin: 29
        delegate: Item {
            x: 5
            width: parent.width
            height: 20
            Row {
                id: row1

                Text {
                    text: name
                    anchors.verticalCenter: parent.verticalCenter
                    font.bold: true
                }
                spacing: 10
            }
            MouseArea {
                id: openArea
                anchors.fill: parent
                onClicked: {
                    console.log("model clicked: " + url)
                    root.visible = false
                    openRegatta(url)
                }
            }
        }

        model: regattas
    }
}

