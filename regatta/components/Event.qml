import QtQuick 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.2


TabView {
    id: tabView

    property var regatta
    property var event

    Tab {
        anchors.margins: 10
        title: "Event"

        GridLayout {
            id: gridLayout
            columns: 4
            columnSpacing: 10
            rowSpacing: 10
            flow: GridLayout.LeftToRight
            anchors.fill: parent

            Label { text: "Title" }
            TextField {
                text: event.name
                onTextChanged: event.name = text
                Layout.columnSpan: 3
                Layout.fillWidth: true
            }


            Label { text: "Mode" }
            ComboBox {
                model: event.modes
                currentIndex: {
                    event.mode
                }
                onCurrentIndexChanged: event.mode = currentIndex
                Layout.columnSpan: 3
                Layout.fillWidth: true
            }


            Label { text: "Date" }
            DatePicker {
                Layout.fillWidth: true
                selectedDate: event.start_date
                onDateChanged: event.start_date = date
            }
            Label {
                text: "until"
                Layout.alignment: Qt.AlignHCenter
            }
            DatePicker {
                Layout.fillWidth: true
                selectedDate: event.end_date
                onDateChanged: event.end_date = date
            }


            Label { text: "Race count" }
            SpinBox {
                Layout.minimumWidth: 100
                Layout.fillWidth: true
                value: event.race_count
                onValueChanged: event.race_count = value
            }
            Label {
                text: "unrated on"
                Layout.alignment: Qt.AlignHCenter
            }
            TextField {
                placeholderText: "E.g. 5,7,10"
                Layout.minimumWidth: 100
                Layout.fillWidth: true
            }


            Label { text: "Organizer" }
            RowLayout {
                Layout.columnSpan: 3
                Layout.fillWidth: true
                spacing: 10
                ComboBox {
                    Layout.columnSpan: 2
                    Layout.fillWidth: true
                    model: regatta.sailing_clubs
                    textRole: 'name'
                }
                Button {
                    iconSource: "icons/ic_create_black_18px.svg"
                }
            }


            Label { text: "Race committee" }
            RowLayout {
                Layout.columnSpan: 3
                Layout.fillWidth: true
                spacing: 10
                ComboBox {
                    Layout.columnSpan: 2
                    Layout.fillWidth: true
                }
                Button {
                    iconSource: "icons/ic_create_black_18px.svg"
                }
            }


            Label { text: "Umpire" }
            RowLayout {
                Layout.columnSpan: 3
                Layout.fillWidth: true
                spacing: 10
                ComboBox {
                    Layout.fillWidth: true
                }
                Button {
                    iconSource: "icons/ic_create_black_18px.svg"
                }
            }


            Label {
                Layout.alignment: Qt.AlignTop
                text: "Assistants"
            }
            RowLayout {
                Layout.columnSpan: 3
                Layout.fillWidth: true
                spacing: 10
                TableView {
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    TableViewColumn {
                        role: "name"
                        title: "Name"
                    }
                    model: assistants
                }
                ColumnLayout {
                    Layout.alignment: Qt.AlignTop
                    spacing: 10
                    Button {
                        iconSource: "icons/ic_create_black_18px.svg"
                    }
                    Button {
                        iconSource: "icons/ic_delete_black_18px.svg"
                    }
                }
            }
        }
    }

    Tab {
        title: "Participants"
    }

}



