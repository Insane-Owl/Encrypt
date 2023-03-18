# Attribution
# lock icon made by freepik from www.flaticon.com

import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

import pyperclip
import functions

from app_window import Ui_MainWindow


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.generateButton.clicked.connect(self.generate_key)
        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.decrypt)
        self.copyButton.clicked.connect(self.copy_output)

    @qtc.Slot()
    def generate_key(self):
        self.keyInput.setText(functions.generate_key())

    def encrypt(self):
        self.outputField.setText(functions.encrypt(self.messageInput.toPlainText(), self.keyInput.text()))

    def decrypt(self):
        self.outputField.setText(functions.decrypt(self.messageInput.toPlainText(), self.keyInput.text()))

    def copy_output(self):
        pyperclip.copy(self.outputField.toPlainText())


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())