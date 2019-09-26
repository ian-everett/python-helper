"""
Example of Qt PySide2 with a native Qt application
"""
import sys
import random
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QVBoxLayout


class MyWidget(QWidget):
    """
    Subclass QWidget and create a simple widget with
    a label and button, when button is pressed the
    label will randomly display a different greeting
    """
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QPushButton("Click me!")
        self.text = QLabel("Hello World")
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        # pylint: disable=E1101
        self.button.clicked.connect(self.magic)

    def magic(self):
        """
        Update text label with a randomly generated greeting message
        """
        self.text.setText(random.choice(self.hello))


def main():
    """
    Entry point into program
    """
    app = QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
