import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import menu
import chart

def m_main():
    app = QApplication(sys.argv)
    win = QMainWindow()  # 创建一个窗口
    loginUi = menu.Ui_MainWindow()  # 创建一个窗口的具体样式
    loginUi.setupUi(win)
    loginUi.groupBox.show()
    loginUi.groupBox_2.hide()


    def charge_1():
        loginUi.groupBox.show()
        loginUi.groupBox_2.hide()
        loginUi.price_bar()


    def charge_2():
        loginUi.groupBox.hide()
        loginUi.groupBox_2.show()
        loginUi.pie_chart()


    loginUi.pushButton.clicked.connect(charge_1)
    loginUi.pushButton_2.clicked.connect(charge_2)

    win.show()
    sys.exit(app.exec_())
