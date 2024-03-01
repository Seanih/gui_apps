# create a basic window
import sys
from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QLabel,
    QPushButton,
    QLineEdit,
    QFormLayout,
    QComboBox,
    QTextEdit,
    QStackedLayout,
    QVBoxLayout,
    QMenuBar,
    QMainWindow,
)
from PyQt6.QtGui import QAction  # menu bar actions


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("GUI Menus")
        self.setGeometry(100, 100, 400, 300)
    
        # create menu bar
        menubar = self.menuBar()
        # menubar.setNativeMenuBar(False)
        
        # create menu items
        file_menu = menubar.addMenu("File")
        edit_menu = menubar.addMenu("Edit")

        # create actions
        self.new_action = QAction("New")
        self.close_action = QAction("Close")
        self.copy_action = QAction("Copy")
        self.cut_action = QAction("Cut")
        self.paste_action = QAction("Paste")

        # add action to menu
        file_menu.addAction(self.new_action)
        # add a separator
        file_menu.addSeparator()

        file_menu.addAction(self.close_action)
        edit_menu.addAction(self.copy_action)
        edit_menu.addAction(self.cut_action)
        edit_menu.addAction(self.paste_action)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
