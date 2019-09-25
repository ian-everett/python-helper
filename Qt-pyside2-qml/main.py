'''Example of Qt PySide using a qml file for Ui'''
from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl


def main():
    '''main entry point'''
    app = QApplication([])

    view = QQuickView()
    view.setSource(QUrl("view.qml"))
    view.show()
    app.exec_()

if __name__ == '__main__':
    main()
