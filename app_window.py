# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextBrowser, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 500)
        MainWindow.setMinimumSize(QSize(300, 500))
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Icon/lock.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.generateButton = QPushButton(self.frame)
        self.generateButton.setObjectName(u"generateButton")

        self.gridLayout_2.addWidget(self.generateButton, 2, 2, 1, 1)

        self.keyInput = QLineEdit(self.frame)
        self.keyInput.setObjectName(u"keyInput")

        self.gridLayout_2.addWidget(self.keyInput, 2, 0, 1, 2)

        self.messageInput = QPlainTextEdit(self.frame)
        self.messageInput.setObjectName(u"messageInput")

        self.gridLayout_2.addWidget(self.messageInput, 0, 0, 1, 3)


        self.gridLayout.addWidget(self.frame, 0, 2, 1, 2)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)


        self.gridLayout.addWidget(self.frame_2, 3, 2, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 2, 1, 2)

        self.frame1 = QFrame(self.centralwidget)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.encryptButton = QPushButton(self.frame1)
        self.encryptButton.setObjectName(u"encryptButton")

        self.horizontalLayout.addWidget(self.encryptButton)

        self.decryptButton = QPushButton(self.frame1)
        self.decryptButton.setObjectName(u"decryptButton")

        self.horizontalLayout.addWidget(self.decryptButton)


        self.gridLayout.addWidget(self.frame1, 1, 2, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 2, 1, 2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.outputField = QTextBrowser(self.frame_3)
        self.outputField.setObjectName(u"outputField")
        self.outputField.setMaximumSize(QSize(16777215, 80))
        self.outputField.setAcceptRichText(False)

        self.horizontalLayout_3.addWidget(self.outputField)

        self.copyButton = QPushButton(self.frame_3)
        self.copyButton.setObjectName(u"copyButton")
        self.copyButton.setMinimumSize(QSize(0, 82))
        self.copyButton.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_3.addWidget(self.copyButton)


        self.gridLayout.addWidget(self.frame_3, 5, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.messageInput, self.keyInput)
        QWidget.setTabOrder(self.keyInput, self.generateButton)
        QWidget.setTabOrder(self.generateButton, self.encryptButton)
        QWidget.setTabOrder(self.encryptButton, self.decryptButton)
        QWidget.setTabOrder(self.decryptButton, self.outputField)
        QWidget.setTabOrder(self.outputField, self.copyButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.keyInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key", None))
        self.messageInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.encryptButton.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.decryptButton.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.outputField.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.copyButton.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
    # retranslateUi

