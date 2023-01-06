# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 270)
        icon = QIcon()
        icon.addFile(u"./static/icons/favicon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.title = QLabel(Form)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(310, 10, 80, 35))
        font = QFont()
        font.setFamilies([u"Hack"])
        font.setPointSize(20)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setFrameShape(QFrame.Box)
        self.title.setAlignment(Qt.AlignCenter)
        self.name = QLabel(Form)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(10, 60, 60, 30))
        font1 = QFont()
        font1.setFamilies([u"Hack"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.name.setFont(font1)
        self.data_path = QLabel(Form)
        self.data_path.setObjectName(u"data_path")
        self.data_path.setGeometry(QRect(10, 100, 120, 30))
        self.data_path.setFont(font1)
        self.data_path.setFrameShape(QFrame.NoFrame)
        self.save_path = QLabel(Form)
        self.save_path.setObjectName(u"save_path")
        self.save_path.setGeometry(QRect(10, 140, 120, 60))
        self.save_path.setFont(font1)
        self.save_path.setFrameShape(QFrame.NoFrame)
        self.name_info = QLineEdit(Form)
        self.name_info.setObjectName(u"name_info")
        self.name_info.setGeometry(QRect(140, 60, 500, 30))
        font2 = QFont()
        font2.setFamilies([u"Hack"])
        font2.setPointSize(14)
        self.name_info.setFont(font2)
        self.data_path_info = QLabel(Form)
        self.data_path_info.setObjectName(u"data_path_info")
        self.data_path_info.setGeometry(QRect(140, 100, 500, 30))
        self.data_path_info.setFont(font2)
        self.data_path_info.setFrameShape(QFrame.Box)
        self.save_path_info = QLabel(Form)
        self.save_path_info.setObjectName(u"save_path_info")
        self.save_path_info.setGeometry(QRect(140, 155, 500, 30))
        self.save_path_info.setFont(font2)
        self.save_path_info.setFrameShape(QFrame.Box)
        self.data_button = QPushButton(Form)
        self.data_button.setObjectName(u"data_button")
        self.data_button.setGeometry(QRect(640, 100, 30, 30))
        icon1 = QIcon()
        icon1.addFile(u"./static/icons/dir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.data_button.setIcon(icon1)
        self.data_button.setIconSize(QSize(30, 30))
        self.save_button = QPushButton(Form)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(640, 155, 30, 30))
        self.save_button.setIcon(icon1)
        self.save_button.setIconSize(QSize(30, 30))
        self.submit = QPushButton(Form)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(325, 220, 50, 30))
        self.submit.setFont(font2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u914d\u7f6e", None))
        self.title.setText(QCoreApplication.translate("Form", u"\u914d\u7f6e", None))
        self.name.setText(QCoreApplication.translate("Form", u"\u59d3\u540d", None))
        self.data_path.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u6587\u4ef6\u5939", None))
        self.save_path.setText(QCoreApplication.translate("Form", u"\u6807\u6ce8\u6587\u4ef6\n"
"\u5b58\u50a8\u8def\u5f84", None))
        self.data_path_info.setText("")
        self.save_path_info.setText("")
        self.data_button.setText("")
        self.save_button.setText("")
        self.submit.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
    # retranslateUi

