# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from DataB import Db_R
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
import fanyi
import main
import quanju
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1009, 661)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 60, 320, 480))
        self.label.setStyleSheet("border-image: url(:/background/img/22.png);\n"
"border-top-left-radius:30px;\n"
"border-bottom-left-radius:30px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 60, 480, 480))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0227273, y1:0.034, x2:1, y2:1, stop:0 rgba(82, 169, 255, 228), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(450, 70, 421, 91))
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 40, 341, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_1 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("#pushButton_1{\n"
"border:none;\n"
"}\n"
"#pushButton_1:focus{\n"
"color:rgb(186,186,186)\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout.addWidget(self.pushButton_1)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"border:none;\n"
"}\n"
"#pushButton_2:focus{\n"
"color:rgb(186,186,186)\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(380, 0, 41, 41))
        self.pushButton.setStyleSheet("border-image: url(:/icon/icon/??????.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(340, 0, 41, 41))
        self.pushButton_6.setStyleSheet("border-image: url(:/icon/icon/??????.png);")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(420, 160, 465, 365))
        self.widget_2.setObjectName("widget_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(150, 40, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 110, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 230, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(120, 38, 26, 150), stop:1 rgba(255, 255, 255, 255));\n"
" color:rgba(255,255,255,220);\n"
" border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_3:hover{\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(120, 38, 26,150));\n"
"}\n"
"QPushButton#pushButton_3:pressed{\n"
" padding-left:5px;\n"
" padding-top:5px;\n"
" background-color:rgba(120,38,26,255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(40, 40, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(40, 110, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox.setGeometry(QtCore.QRect(50, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(420, 160, 465, 365))
        self.widget_3.setObjectName("widget_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 100, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 150, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 310, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton#pushButton_5{\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(120, 38, 26, 150), stop:1 rgba(255, 255, 255, 255));\n"
" color:rgba(255,255,255,220);\n"
" border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_5:hover{\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(120, 38, 26,150));\n"
"}\n"
"QPushButton#pushButton_5:pressed{\n"
" padding-left:5px;\n"
" padding-top:5px;\n"
" background-color:rgba(120,38,26,255);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(40, 100, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(40, 150, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setGeometry(QtCore.QRect(40, 20, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(40, 50, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(150, 250, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_11 = QtWidgets.QLabel(self.widget_3)
        self.label_11.setGeometry(QtCore.QRect(40, 250, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(150, 200, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;")
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_12 = QtWidgets.QLabel(self.widget_3)
        self.label_12.setGeometry(QtCore.QRect(40, 200, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 130, 141, 31))
        self.label_5.setStyleSheet("font: 18pt \"??????\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 170, 101, 31))
        self.label_6.setStyleSheet("font: 18pt \"??????\";\n"
"")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        # self.pushButton_3.clicked.connect(self.Lg)
        self.change_widget2()
        self.pushButton_1.clicked.connect(self.change_widget2)
        self.pushButton_2.clicked.connect(self.change_widget3)
        self.pushButton_3.clicked.connect(self.Lg)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def Lg(self):
        user_1 = self.lineEdit.text()
        password_1 = self.lineEdit_2.text()
        sql = "select * from user"
        user = Db_R(sql)
        for i in range(len(user)):
            if user['name'][i] == user_1 and user['passwd'][i] == password_1:
                quanju.fanyi_win = QMainWindow()
                self.fanyiUi = fanyi.Ui_MainWindow()
                self.fanyiUi.setupUi(quanju.fanyi_win)
                quanju.fanyi_win.show()
                quanju.login_win.close()
                break
    def change_widget3(self):
        self.widget_2.hide()
        self.widget_3.show()
    def change_widget2(self):
        self.widget_3.hide()
        self.widget_2.show()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_1.setText(_translate("MainWindow", "??????"))
        self.pushButton_2.setText(_translate("MainWindow", "??????"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "???????????????"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "???????????????"))
        self.pushButton_3.setText(_translate("MainWindow", "???     ???"))
        self.label_3.setText(_translate("MainWindow", "???     ???"))
        self.label_4.setText(_translate("MainWindow", "???     ???"))
        self.checkBox.setText(_translate("MainWindow", "????????????"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "???????????????"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "???????????????"))
        self.pushButton_5.setText(_translate("MainWindow", "???     ???"))
        self.label_7.setText(_translate("MainWindow", "???     ???"))
        self.label_8.setText(_translate("MainWindow", "???     ???"))
        self.label_9.setText(_translate("MainWindow", "????????????????????????"))
        self.label_10.setText(_translate("MainWindow", "????????????????????????"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "??????????????????"))
        self.label_11.setText(_translate("MainWindow", " ??? ??? ???"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "???????????????"))
        self.label_12.setText(_translate("MainWindow", "??? ??? ??? ???"))
        self.label_5.setText(_translate("MainWindow", "????????????"))
        self.label_6.setText(_translate("MainWindow", "????????????"))
import test_rc
