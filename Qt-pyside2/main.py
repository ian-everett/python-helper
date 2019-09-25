'''Example of Qt PySide using qml file and a paint item'''
import sys
from PySide2.QtCore import Signal, QTimer, Slot, QUrl
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import qmlRegisterType
from PySide2.QtQuick import QQuickPaintedItem, QQuickView


class Bar(QQuickPaintedItem):
    '''child of QQuickPaintedItem'''
    def __init__(self, parent=None):
        QQuickPaintedItem.__init__(self, parent)
        timer = QTimer(self)
        timer.timeout.connect(self.timed_out)
        timer.start(1000)

    def paint(self, painter):
        painter.drawRect(0, 0, 50, 50)

    # pylint: disable=R0201
    def timed_out(self):
        '''1 second timer has timed out'''
        print("Update")

    chartCleared = Signal()

    @Slot()
    def clear_chart(self):
        '''this can be called via the qml file'''
        self.update()

def main():
    '''main entry point'''
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

if __name__ == '__main__':
    main()
