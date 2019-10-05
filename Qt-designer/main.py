"""
Example of Qt PySide2 with a native Qt application loading the Ui file
"""
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtWidgets import QWidget


class MainWindow(QWidget):
    """
    Subclass QWidget and create a widget reading
    from a given ui file
    """
    def __init__(self, ui_file):
        super().__init__()

        # Open ui file
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)

        # Load the ui
        loader = QUiLoader()
        ui_interface = loader.load(ui_file, self)
        ui_file.close()

        # Assign the ui controls to some refrences for easy access
        self.button = ui_interface.button
        self.label = ui_interface.label

        # pylint: disable=E1101
        self.button.clicked.connect(self.update)

        self.label.setText('')
        self.count = 0

    def update(self):
        """
        Update text label with a greeting message
        """
        self.count += 1
        self.label.setText(str(self.count))
        print(self.label.text())



def main():
    """
    Entry point into program
    """
    app = QApplication([])

    # Create main window from a ui file and show it
    window = MainWindow('frame.ui')
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
