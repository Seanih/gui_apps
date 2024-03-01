# create a basic window
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QTextEdit,
    QMenuBar,
    QMenu,
    QMainWindow,
    QFileDialog,
    QInputDialog,
)

from PyQt6.QtGui import QAction, QTextCursor, QColor, QIcon
from PyQt6.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Notepad")
        self.setGeometry(100, 100, 400, 300)

        self.current_file_path = None

        # create text field and make it the central widget
        self.text_edit_field = QTextEdit(self)
        self.setCentralWidget(self.text_edit_field)

        # create menu bar
        menubar = QMenuBar(self)
        menubar.setNativeMenuBar(False)  # show menubar in app
        self.setMenuBar(menubar)

        # create file menu
        file_menu = QMenu("File", self)
        menubar.addMenu(file_menu)

        # create edit menu
        edit_menu = QMenu("Edit", self)
        menubar.addMenu(edit_menu)

        # create actions and connect functions
        new_action = QAction("New", self)
        file_menu.addAction(new_action)
        new_action.triggered.connect(self.new_file)

        open_action = QAction("Open", self)
        file_menu.addAction(open_action)
        open_action.triggered.connect(self.open_file)

        save_action = QAction("Save", self)
        file_menu.addAction(save_action)
        save_action.triggered.connect(self.save_file)

        save_file_as_action = QAction("Save As", self)
        file_menu.addAction(save_file_as_action)
        save_file_as_action.triggered.connect(self.save_file_as)

        edit_action = QAction("Edit", self)
        edit_menu.addAction(edit_action)
        edit_action.triggered.connect(self.edit_file)

        # * undo, redo, cut, copy & paste are built in functions
        undo_action = QAction("Undo", self)
        edit_menu.addAction(undo_action)
        undo_action.triggered.connect(self.text_edit_field.undo)

        redo_action = QAction("Redo", self)
        edit_menu.addAction(redo_action)
        redo_action.triggered.connect(self.text_edit_field.redo)

        cut_action = QAction("Cut", self)
        edit_menu.addAction(cut_action)
        cut_action.triggered.connect(self.text_edit_field.cut)

        copy_action = QAction("Copy", self)
        edit_menu.addAction(copy_action)
        copy_action.triggered.connect(self.text_edit_field.copy)

        paste_action = QAction("Paste", self)
        edit_menu.addAction(paste_action)
        paste_action.triggered.connect(self.text_edit_field.paste)

        find_action = QAction("Find", self)
        edit_menu.addAction(find_action)
        find_action.triggered.connect(self.find_text)

        # * -----create TOOLBAR and connect actions----
        toolbar = self.addToolBar("Main Toolbar")
        # add icon to toolbar with text hint
        self.new_file_toolbar_action = QAction(QIcon("icons/new_icon.png"), "New File")
        self.new_file_toolbar_action.triggered.connect(self.new_file)
        toolbar.addAction(self.new_file_toolbar_action)

        self.open_toolbar_action = QAction(QIcon("icons/open_icon.png"), "Open File")
        self.open_toolbar_action.triggered.connect(self.open_file)
        toolbar.addAction(self.open_toolbar_action)

        toolbar.addSeparator()

        self.save_toolbar_action = QAction("Save")
        self.save_toolbar_action = QAction(QIcon("icons/save_icon.png"), "Save File")
        self.save_toolbar_action.triggered.connect(self.save_file)
        toolbar.addAction(self.save_toolbar_action)
        # * -----create TOOLBAR and add actions-----

    def new_file(self):
        self.text_edit_field.clear()
        self.current_file_path = None

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "", "All Files(*);; Python Files(*.py)"
        )

        if file_path:
            with open(file_path, "r") as file:
                self.text_edit_field.setText(file.read())

    def save_file_as(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "All files(*);; Python File(*.py)"
        )

        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_edit_field.toPlainText())
            self.current_file_path = file_path

    def save_file(self):
        if self.current_file_path:
            with open(self.current_file_path, "w") as file:
                file.write(self.text_edit_field.toPlainText())
        else:
            self.save_file_as()

    def edit_file(self):
        print("edit file")

    def find_text(self):
        print("Found Text")
        search_text, text_found = QInputDialog.getText(self, "Find Text", "Seach for:")

        if text_found:
            all_words = []

            self.text_edit_field.moveCursor(QTextCursor.MoveOperation.Start)

            highlight_color = QColor(Qt.GlobalColor.blue)

            while self.text_edit_field.find(search_text):
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(highlight_color)

                selection.cursor = self.text_edit_field.textCursor()
                all_words.append(selection)
            self.text_edit_field.setExtraSelections(all_words)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
