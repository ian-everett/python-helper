import sys, os
from PySide2.QtCore import Property, Signal, QTimer, Slot, QUrl, Qt
from PySide2.QtGui import QGuiApplication, QPainter
from PySide2.QtQml import qmlRegisterType
from PySide2.QtQuick import QQuickPaintedItem, QQuickView

class Bar(QQuickPaintedItem):
    def __init__(self, parent = None):
        QQuickPaintedItem.__init__(self, parent)
        timer = QTimer(self)
        timer.timeout.connect(self.hasTimedOut)
        timer.start(1000)

    def paint(self, painter):
        painter.drawRect(0, 0, 50, 50)
    
    def hasTimedOut(self):
        print("Update")
        
    chartCleared = Signal()

    @Slot() # This should be something like @Invokable
    def clearChart(self):
        self.update()


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)

    qmlRegisterType(Bar, 'Charts', 1, 0, 'Bar')

    view = QQuickView()
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.setSource(QUrl.fromLocalFile('app.qml'))
    view.show()
    res = app.exec_()

    # Deleting the view before it goes out of scope is required to make sure all child QML instances
    # are destroyed in the correct order.
    del view
    sys.exit(res)