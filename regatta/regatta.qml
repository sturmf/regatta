import QtQuick 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.2
import "DatePicker"


TabView {
    id: tabView

    property var regatta

    Tab {
        anchors.margins: 10
        title: "Regatta"

        GridLayout {
            id: gridLayout
            columns: 4
            columnSpacing: 10
            rowSpacing: 10
            flow: GridLayout.LeftToRight
            anchors.fill: parent

            Label { text: "Title" }
            TextField {
                text: regatta.name
                onTextChanged: regatta.name = text
                Layout.columnSpan: 3
                Layout.fillWidth: true
            }


            Label { text: "Modus" }
            ComboBox {
                model: regatta.modes
                currentIndex: regatta.modus
                onCurrentIndexChanged: regatta.modus = currentIndex
                Layout.columnSpan: 3
                Layout.fillWidth: true
            }


            Label { text: "Date" }
            DatePicker {
                Layout.fillWidth: true
                selectedDate: regatta.start_date
                onDateChanged: regatta.start_date = date
            }
            Label {
                text: "until"
                Layout.alignment: Qt.AlignHCenter
            }
            DatePicker {
                Layout.fillWidth: true
                selectedDate: regatta.end_date
                onDateChanged: regatta.end_date = date
            }


            Label { text: "Race count" }
            SpinBox {
                Layout.minimumWidth: 100
                Layout.fillWidth: true
                value: regatta.race_count
                onValueChanged: regatta.race_count = value
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



