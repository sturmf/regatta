import QtQuick 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.2
import "DatePicker"

TabView {
    id: tabView

    property var regatta

    Tab {
        anchors.margins: 5
        title: "Regatta"

        GridLayout {
            id: gridLayout
            columns: 4
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
                ComboBox {
                    Layout.columnSpan: 2
                    Layout.fillWidth: true
                }
                Button {
                    text: "+"
                }
            }


            Label { text: "Race committee" }
            RowLayout {
                Layout.columnSpan: 3
                Layout.fillWidth: true
                ComboBox {
                    Layout.columnSpan: 2
                    Layout.fillWidth: true
                }
                Button {
                    text: "+"
                }
            }


            Label { text: "Umpire" }
            RowLayout {
                Layout.columnSpan: 3
                Layout.fillWidth: true
                ComboBox {
                    Layout.fillWidth: true
                }
                Button {
                    text: "+"
                }
            }


            Label {
                text: "Assistants"
            }
            RowLayout {
                Layout.columnSpan: 3
                Layout.fillWidth: true
                ComboBox {
                    Layout.fillWidth: true
                }
                Button {
                    text: "Add"
                }
                Button {
                    text: "+"
                }
            }


            Label {}
            TableView {
                Layout.columnSpan: 3
                Layout.fillWidth: true
                Layout.fillHeight: true
                TableViewColumn {
                    role: "name"
                    title: "Name"
                }
                model: assistants
            }

        }
    }

    Tab {
        title: "Participants"
    }

}



