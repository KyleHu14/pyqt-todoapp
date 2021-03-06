from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 632)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addItem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.add_task())
        self.addItem_pushButton.setGeometry(QtCore.QRect(10, 70, 161, 41))
        self.addItem_pushButton.setObjectName("addItem_pushButton")
        self.addItem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addItem_lineEdit.setGeometry(QtCore.QRect(10, 20, 501, 41))
        self.addItem_lineEdit.setObjectName("addItem_lineEdit")
        self.myList_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.myList_listWidget.setGeometry(QtCore.QRect(10, 120, 501, 461))
        self.myList_listWidget.setObjectName("myList_listWidget")
        self.deleteItem_pushButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.delete_task())
        self.deleteItem_pushButton.setGeometry(QtCore.QRect(190, 70, 151, 41))
        self.deleteItem_pushButton.setObjectName("deleteItem_pushButton")
        self.clearAll_pushButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.clear_list())
        self.clearAll_pushButton.setGeometry(QtCore.QRect(360, 70, 151, 41))
        self.clearAll_pushButton.setObjectName("clearAll_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 521, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Add Item to List
    def add_task(self):
        # .text() grabs whatever is in the box and puts it into task
        task = self.addItem_lineEdit.text()

        # Add item to list
        self.myList_listWidget.addItem(task)

        # Clear task field
        self.addItem_lineEdit.setText('')

    # Delete Item from List
    def delete_task(self):
        # Grab selected row
        selected_task = self.myList_listWidget.currentRow()

        # Delete selected row 
        self.myList_listWidget.takeItem(selected_task)

    # Clear List
    def clear_list(self):
        self.myList_listWidget.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do List"))
        self.addItem_pushButton.setText(_translate("MainWindow", "Add Task"))
        self.deleteItem_pushButton.setText(_translate("MainWindow", "Delete Task"))
        self.clearAll_pushButton.setText(_translate("MainWindow", "Clear List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
