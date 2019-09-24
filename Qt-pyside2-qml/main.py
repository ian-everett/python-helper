from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl


app = QApplication([])

view = QQuickView()
view.setSource(QUrl("view.qml"))
view.show()

app.exec_()