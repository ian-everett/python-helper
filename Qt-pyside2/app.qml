import Charts 1.0
import QtQuick 2.0

Item {
    id: rootId

    width: 800
    height: 600

    Rectangle {
        id: rectId

        Bar {
            anchors.centerIn: parent
        }

        anchors.fill: parent
        anchors.margins: 100
        border.width: 5
        radius: 5
    }
}
