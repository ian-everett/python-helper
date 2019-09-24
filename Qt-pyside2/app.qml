import QtQuick 2.0

Item {
    id: rootId

    width: 800
    height: 600

    Rectangle {
        id: rectId

        anchors.fill: parent
        anchors.margins: 100
        color: 'red'
        border.width: 2
        radius: 5
    }
}
