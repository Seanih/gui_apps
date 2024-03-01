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
    QVBoxLayout
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Form Layout")
        self.setGeometry(100, 100, 400, 300)

        self.combo_box = QComboBox()
        self.combo_box.addItems(["Label", "Form"])
        self.combo_box.activated.connect(self.changePage)

        # page 1
        label_page = QLabel("This is the Label Page")
        
        # page 2
        form = QFormLayout()
        form.addRow("", QLabel("Form Page foo!"))
        page2_container = QWidget()
        page2_container.setLayout(form)
        
        # create stack layout
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(label_page)
        self.stacked_layout.addWidget(page2_container)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.combo_box)
        main_layout.addLayout(self.stacked_layout)
        
        self.setLayout(main_layout) 
        
    def changePage(self, index):
        self.stacked_layout.setCurrentIndex(index)
                   


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
