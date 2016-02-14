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
                onEditingFinished: regatta.name = text
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
            }
            Label {
                text: "until"
                Layout.alignment: Qt.AlignHCenter
            }
            DatePicker {
                Layout.fillWidth: true
            }


            Label { text: "Race count" }
            SpinBox {
                Layout.minimumWidth: 100
                Layout.fillWidth: true
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
            ScrollView {
                Layout.columnSpan: 3
                Layout.fillWidth: true
                Layout.fillHeight: true
                frameVisible: true
                verticalScrollBarPolicy: Qt.ScrollBarAlwaysOn
                ListView {
                    delegate: Text {
                            text: name
                    }
                    model: assistants
                }
            }
        }
    }

    Tab {
        title: "Participants"
    }

}



