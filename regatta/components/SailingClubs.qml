import QtQuick 2.0
import QtQuick.Window 2.2
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.3
import QSailingClub 1.0
import "helper.js" as Helper

// FIXME: move KeyPress handlers out into actions / functions

Window {
    id: root

    property var regatta
    property var event
    property var selectedSailingClub

    signal sailingClubCreated(QSailingClub sailing_club) // fixme should be a function
    signal sailingClubSelected(QSailingClub sailing_club)

    width: 800
    height: 400

    modality: Qt.WindowModal

    onSailingClubCreated: selectedSailingClub = sailing_club
    Component.onCompleted: { regatta.sailingClubCreated.connect(root.sailingClubCreated) }

    Item {
        width: parent.width
        height: parent.height
        focus: true

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
                                onClicked: regatta.new_sailing_club()
                            }
                            Button {
                                id: removeButton
                                anchors.right: parent.right
                                iconSource: "icons/ic_delete_black_18px.svg"
                                onClicked: {
                                    regatta.delete_sailing_club(selectedSailingClub)
                                }
                            }
                        }
                        TableView {
                            id: sailing_club_table
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
                            model: regatta.sailing_clubs
                            //onSortIndicatorColumnChanged: model.sort(sortIndicatorColumn, sortIndicatorOrder)
                            //onSortIndicatorOrderChanged: model.sort(sortIndicatorColumn, sortIndicatorOrder)
                            onClicked: selectedSailingClub = model.get(row)
                            onDoubleClicked: {
                                sailingClubSelected(selectedSailingClub)
                                root.close()
                            }
                            onActivated: {
                                selectedSailingClub = model.get(row)
                            }
                            Component.onCompleted: {
                                var index = Helper.getIndex(model, selectedSailingClub)
                                sailing_club_table.selection.select(index, index)
                                sailing_club_table.positionViewAtRow(index, ListView.Contain)
                            }
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
                                text: selectedSailingClub ? selectedSailingClub.name : ''
                                enabled: selectedSailingClub ? true : false
                                onTextChanged: if (selectedSailingClub) selectedSailingClub.name = text
                            }

                            Label {
                                text: "Abbreviation"
                            }
                            TextField {
                                Layout.fillWidth: true
                                text: selectedSailingClub ? selectedSailingClub.abbreviation : ''
                                enabled: selectedSailingClub ? true : false
                                onTextChanged: if (selectedSailingClub) selectedSailingClub.abbreviation = text
                            }

                            Label {
                                text: "DSV number"
                            }
                            TextField {
                                Layout.fillWidth: true
                                text: selectedSailingClub ? selectedSailingClub.registration : ''
                                enabled: selectedSailingClub ? true : false
                                onTextChanged: if (selectedSailingClub) selectedSailingClub.registration = text
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
                    onClicked : {
                        sailingClubSelected(selectedSailingClub)
                        root.close()
                    }
                    Keys.onPressed: if (event.key === Qt.Key_Return) {
                        sailingClubSelected(selectedSailingClub)
                        root.close()
                    }
                }
                Button {
                    text: "Cancel"
                    onClicked: root.close()
                    Keys.onPressed: if (event.key === Qt.Key_Return) { root.close() }
                }
            }

        }

        Keys.onEscapePressed: root.close()
    }
}
