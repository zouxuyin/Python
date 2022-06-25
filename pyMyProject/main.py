import sys
import testUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from DataB import Db_R
import fanyi
import quanju

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    quanju.login_win  = QMainWindow()
    myUI = testUi.Ui_MainWindow()
    myUI.setupUi(quanju.login_win)
    quanju.login_win.show()
    sys.exit(myapp.exec_())