import QtQuick 2.0
import QtQuick.Window 2.2
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.3

Window {
    id: root

    width: 800
    height: 400

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10
        SplitView {
            id: splitView1
            anchors.fill: parent

            ColumnLayout {
                Layout.fillWidth: true
                ColumnLayout {
                    anchors.fill: parent
                    anchors.rightMargin: 15
                    spacing: 10

                    Label {
                        text: qsTr("Available sailing clubs")
                        font.bold: true
                    }
                    RowLayout {
                        id: rowLayout1
                        anchors.left: parent.left
                        anchors.right: parent.right

                        TextField {
                            height: 20
                            anchors.right: addButton.left
                            anchors.rightMargin: 10
                            anchors.left: parent.left
                            placeholderText: "Search"
                            Layout.fillWidth: true
                        }
                        Button {
                            id: addButton
                            anchors.right: removeButton.left
                            anchors.rightMargin: 10
                            iconSource: "icons/ic_note_add_black_18px.svg"
                        }
                        Button {
                            id: removeButton
                            anchors.right: parent.right
                            iconSource: "icons/ic_delete_black_18px.svg"
                        }
                    }
                    TableView {
                        anchors.top: rowLayout1.bottom
                        anchors.bottom: parent.bottom
                        anchors.right: parent.right
                        anchors.left: parent.left
                        anchors.topMargin: 10
                        Layout.fillHeight: true
                        TableViewColumn {
                            role: "name"
                            title: "Name"
                        }
                        model: sailingclubs
                    }
                }
            }

            ColumnLayout {
                width:  (root.width - 20 )/ 2
                Layout.fillHeight: true
                anchors.top: parent.top
                anchors.bottom: parent.bottom

                ColumnLayout {
                    anchors.fill: parent
                    anchors.leftMargin: 15

                    Label {
                        id: label1
                        text: qsTr("Selected sailing club")
                        font.bold: true
                    }
                    GridLayout {
                        id: grid1
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: label1.bottom
                        anchors.topMargin: 10
                        columns: 2
                        rowSpacing: 10
                        columnSpacing: 10

                        Label {
                            text: "Name"
                        }
                        TextField {
                            Layout.fillWidth: true
                        }

                        Label {
                            text: "Abbreviation"
                        }
                        TextField {
                            Layout.fillWidth: true
                        }

                        Label {
                            text: "DSV number"
                        }
                        TextField {
                            Layout.fillWidth: true
                        }

                    }
                }

            }

        }

        RowLayout {
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            Button {
                text: "Select"
            }
            Button {
                text: "Cancel"
            }
        }

    }
}
