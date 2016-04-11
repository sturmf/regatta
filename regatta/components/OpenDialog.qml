import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Layouts 1.0

Rectangle {
    id: root

    signal newEvent(string name)
    signal openEvent(int index)

    property alias listView: listView

    Button {
        id: newButton
        text: qsTr("New")
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20
        anchors.right: parent.right
        anchors.rightMargin: 20
        onClicked: {
            newEvent(name.text)
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
        placeholderText: qsTr("Event Name")
        onAccepted: {
            newEvent(name.text)
        }
    }

    ListView {
        id: listView
        spacing: 5
        anchors.bottom: name.top
        anchors.right: parent.right
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottomMargin: 20
        anchors.rightMargin: 20
        anchors.leftMargin: 20
        anchors.topMargin: 20
        delegate: Rectangle {
            id: item1
            x: 0
            width: 760
            height: 40
            radius: 4
            gradient: Gradient {
                GradientStop {
                    position: 0.544
                    color: "#ffffff"
                }

                GradientStop {
                    position: 0.074
                    color: "#f4f4f4"
                }

                GradientStop {
                    position: 1.007
                    color: "#f4f4f4"
                }

            }
            border.width: 1
            border.color: "#adadad"
            Row {
                id: row1
                anchors.left: parent.left
                anchors.leftMargin: 5
                spacing: 0
                anchors.verticalCenter: parent.verticalCenter

                Text {
                    text: name
                    font.pointSize: 17
                    anchors.verticalCenter: parent.verticalCenter
                    font.bold: true
                }
            }
            MouseArea {
                id: openArea
                anchors.fill: parent
                onClicked: {
                    console.log("model clicked: " + listView.model[index].name)
                    root.visible = false
                    openEvent(index)
                }
            }
        }

        // This is necessary for dummyData to work
        model: events
    }
}

