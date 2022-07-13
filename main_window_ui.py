# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(633, 336)
        icon = QIcon()
        icon.addFile(u"images/window_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(MainWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit = QPlainTextEdit(MainWindow)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"#widget {\n"
"	background-color: white;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.backgroundImageLabel = QLabel(self.widget)
        self.backgroundImageLabel.setObjectName(u"backgroundImageLabel")
        self.backgroundImageLabel.setMaximumSize(QSize(150, 150))
        self.backgroundImageLabel.setCursor(QCursor(Qt.OpenHandCursor))
        self.backgroundImageLabel.setPixmap(QPixmap(u"images/default_background.png"))
        self.backgroundImageLabel.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.backgroundImageLabel)


        self.verticalLayout.addWidget(self.widget)

        self.verticalLayout.setStretch(0, 25)
        self.verticalLayout.setStretch(1, 75)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(MainWindow)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_2 = QWidget(MainWindow)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"#widget_2 {\n"
"	background-color: white;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.qrcodeLabel = QLabel(self.widget_2)
        self.qrcodeLabel.setObjectName(u"qrcodeLabel")
        self.qrcodeLabel.setMaximumSize(QSize(220, 220))
        self.qrcodeLabel.setCursor(QCursor(Qt.OpenHandCursor))
        self.qrcodeLabel.setPixmap(QPixmap(u"images/default_qrcode.png"))
        self.qrcodeLabel.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.qrcodeLabel)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 42)
        self.horizontalLayout.setStretch(1, 16)
        self.horizontalLayout.setStretch(2, 42)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u827a\u672f\u4e8c\u7ef4\u7801\u751f\u6210\u5668", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7f51\u5740\u6216\u5176\u4ed6\u6587\u672c", None))
        self.backgroundImageLabel.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa\n"
"\u4e8c\u7ef4\u7801", None))
        self.qrcodeLabel.setText("")
    # retranslateUi

