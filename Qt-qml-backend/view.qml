import Interface 1.0
import QtQuick 2.0

Item {
    id: rootId

    Backend {
        id: backendId

        Component.onCompleted: {
            console.log('Backend value = ' + backendId.value)
        }
    }

    width: 800
    height: 600

    Rectangle {
        id: rectId

        anchors.fill: parent
        anchors.margins: 100
        border.width: 5
        radius: 5

        Text {
            id: textId

            anchors.centerIn: parent
            width: parent/4
            height: parent/4

            text: backendId.value
        }
    }
}
