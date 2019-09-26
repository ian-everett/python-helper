"""
Example of Qt PySide2 with a Python backend and qml frontend
typically this use case is for when the front end needs to
do file I/O rather than below.
"""
import sys
from PySide2.QtCore import QObject
from PySide2.QtCore import Property
from PySide2.QtCore import Signal
from PySide2.QtCore import QTimer
from PySide2.QtCore import QUrl
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import qmlRegisterType
from PySide2.QtQuick import QQuickView


class Backend(QObject):
    """
    Backend
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self._value = 42

        # setup a timer to fire every second
        # pylint: disable=E1101
        timer = QTimer(self)
        timer.start(1000)
        timer.timeout.connect(self.update)

    #
    # update
    #
    def update(self):
        """
        inc value counter every second
        """
        self.set_value(self._value + 1)

    #
    # value signal & getter/setter
    #
    @Signal
    def value_changed(self):
        """value changed signal"""

    @Property(int, notify=value_changed)
    def value(self):
        """
        value getter
        """
        return self._value

    @value.setter
    def set_value(self, value):
        """
        value setter
        """
        if value != self._value:
            self._value = value
            # pylint: disable=E1101
            self.value_changed.emit()


def main():
    """
    Entry point into program
    """
    app = QGuiApplication(sys.argv)

    # Register the Backend which can be used in the qml view
    qmlRegisterType(Backend, 'Interface', 1, 0, 'Backend')

    # Create a quickview widget and load the view
    view = QQuickView()
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.setSource(QUrl.fromLocalFile('view.qml'))
    view.show()
    res = app.exec_()

    # Deleting the view before it goes out of scope is required to make
    # sure all child QML instances are destroyed in the correct order.
    # Sept 2019 * Not sure if we still need to do this *
    del view
    sys.exit(res)

if __name__ == '__main__':
    main()
