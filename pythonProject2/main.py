import sys
import index
from PyQt5.QtWidgets import QApplication, QMainWindow



if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    win = QMainWindow()
    myUI = index.Ui_MainWindow()
    myUI.setupUi(win)
    myUI.widget_3.hide()
    myUI.widget_4.hide()
    myUI.widget_5.hide()
    myUI.widget_6.hide()
    def change_widget2():
        myUI.widget_3.hide()
        myUI.widget_4.hide()
        myUI.widget_5.hide()
        myUI.widget_6.hide()
        myUI.widget_2.show()
    def change_widget3():
        myUI.widget_2.hide()
        myUI.widget_4.hide()
        myUI.widget_5.hide()
        myUI.widget_6.hide()
        myUI.widget_3.show()
    def change_widget4():
        myUI.widget_2.hide()
        myUI.widget_3.hide()
        myUI.widget_5.hide()
        myUI.widget_6.hide()
        myUI.widget_4.show()
    def change_widget5():
        myUI.widget_2.hide()
        myUI.widget_3.hide()
        myUI.widget_4.hide()
        myUI.widget_6.hide()
        myUI.widget_5.show()
    def change_widget6():
        myUI.widget_2.hide()
        myUI.widget_3.hide()
        myUI.widget_4.hide()
        myUI.widget_5.hide()
        myUI.widget_6.show()
    myUI.pushButton.clicked.connect(change_widget2)
    myUI.pushButton_2.clicked.connect(change_widget3)
    myUI.pushButton_3.clicked.connect(change_widget4)
    myUI.pushButton_4.clicked.connect(change_widget5)
    myUI.pushButton_5.clicked.connect(change_widget6)
    win.show()
    sys.exit(myapp.exec_())