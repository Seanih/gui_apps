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
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Form Layout")
        self.setGeometry(100, 100, 400, 300)

        form_layout = QFormLayout()
        self.setLayout(form_layout)

        self.name_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.phone_edit = QLineEdit()

        self.subject_combo = QComboBox()
        self.subject_combo.addItems(["Select Subject", "Personal", "Business"])

        self.message_edit = QTextEdit()

        submit_btn = QPushButton("Submit")
        submit_btn.clicked.connect(self.submitClicked)

        form_layout.addRow(QLabel("Name"), self.name_edit)
        form_layout.addRow(QLabel("Email"), self.email_edit)
        form_layout.addRow(QLabel("Phone"), self.phone_edit)
        form_layout.addRow(QLabel("Subject"), self.subject_combo)
        form_layout.addRow(QLabel("Message"), self.message_edit)
        form_layout.addRow(submit_btn)

    def submitClicked(self):
        name = self.name_edit.text()
        email = self.email_edit.text()
        phone = self.phone_edit.text()
        subject = self.subject_combo.currentText()
        message = self.message_edit.toPlainText()

        self.name_edit.setText("")
        self.email_edit.setText("")
        self.phone_edit.setText("")
        self.subject_combo.setCurrentIndex(0)
        self.message_edit.setText("")

        print(
            f"""
                Name: {name}
                Email: {email}
                Phone: {phone}
                Subject: {subject}
                Message: {message}
              """
        )


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
