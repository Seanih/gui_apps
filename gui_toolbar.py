# create a basic window
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
)

from PyQt6.QtGui import QIcon, QAction


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("GUI Menus")
        self.setGeometry(100, 100, 400, 300)

        toolbar = self.addToolBar("Main Toolbar")
        # add icon to toolbar with text hint
        self.new_action = QAction(QIcon("icons/new_icon.png"), "New File")
        toolbar.addAction(self.new_action)

        self.open_action = QAction(QIcon("icons/open_icon.png"), "Open File")
        toolbar.addAction(self.open_action)

        toolbar.addSeparator()

        self.save_action = QAction("Save")
        self.save_action = QAction(QIcon("icons/save_icon.png"), "Save File")
        toolbar.addAction(self.save_action)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
