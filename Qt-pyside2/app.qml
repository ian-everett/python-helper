import Charts 1.0
import QtQuick 2.0

Item {
    width: 800
    height: 600

    Bar {
        id: barId
        anchors.centerIn: parent
        width: 100
        height: 100
    }

    MouseArea {
         anchors.fill: parent
         onClicked: barId.clearChart()
     }

    Text {
        text: "A Bar"
        anchors {
            bottom: parent.bottom;
            horizontalCenter: parent.horizontalCenter;
            bottomMargin: 20
        }
    }
}
