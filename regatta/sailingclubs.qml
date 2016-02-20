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
            Layout.fillWidth: true
            Layout.fillHeight: true

            ColumnLayout {
                Layout.fillWidth: true
                ColumnLayout {
                    anchors.fill: parent
                    anchors.rightMargin: 15

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
                            anchors.rightMargin: 5
                            anchors.left: parent.left
                            anchors.leftMargin: 0
                            placeholderText: "Search"
                            Layout.fillWidth: true
                        }
                        Button {
                            id: addButton
                            anchors.right: parent.right
                            iconSource: "icons/List-add.svg.png"
                        }

                    }
                    TableView {
                        anchors.top: rowLayout1.bottom
                        anchors.bottom: parent.bottom
                        anchors.right: parent.right
                        anchors.left: parent.left
                        anchors.topMargin: 5
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
                width: root.width * 4 / 10 // approx. golden cut
                Layout.fillHeight: true
                anchors.top: parent.top
                anchors.bottom: parent.bottom

                ColumnLayout {
                    anchors.fill: parent
                    //anchors.margins: 5
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
                        anchors.topMargin: 5
                        columns: 2

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
