from PyQt6.QtGui import QFont
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QWidget, QLineEdit, QPushButton, QListWidget
import sys

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        window_title = 'ToDo List'
        window_x = 0 
        window_y = 0
        window_width = 500
        window_height = 400

        self.initUI(window_title, window_x, window_y, window_width, window_height)

    def initUI(self, window_title, window_x, window_y, window_width, window_height):
        # Setting up the Window
        self.setWindowTitle(window_title)
        self.setGeometry(window_x, window_y, window_width, window_height)

        # Setting up the UI
        window_layout = QGridLayout()
        self.setLayout(window_layout)

        # Create the Task Field
        task_field = QLineEdit(self)
        task_field.setPlaceholderText('Enter a Task :')

        # Create Three Buttons (Add Task | Delete Selected Task | Clear Task List)
        add_task = QPushButton('Add a Task', self)
        del_task = QPushButton('Delete Task', self)
        clear_list = QPushButton('Clear All Tasks', self)

        # Create the Task List
        task_list = QListWidget()
        
        # Placing Widgets into the Grid
        # Task Field is placed at (0,0), Takes up 1 row 3 cols
        window_layout.addWidget(task_field, 0, 0, 1, 3)
        # 3 Buttons take up 1 col and collectively 1 row, are placed in row 1
        window_layout.addWidget(add_task, 1, 0)
        window_layout.addWidget(del_task, 1, 1)
        window_layout.addWidget(clear_list, 1, 2)
        # Task List is placed at (2,0), Takes up 1 row and 3 cols
        window_layout.addWidget(task_list, 2, 0, 1, 3)

        self.show()

if __name__ == '__main__':
    application = QApplication([])
    ex = ToDoApp()
    sys.exit(application.exec())