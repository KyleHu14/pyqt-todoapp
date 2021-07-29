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
        self.task_field = QLineEdit(self)
        self.task_field.setPlaceholderText('Enter a Task :')

        # Create the Task List
        self.task_list = QListWidget()

        # Create Three Buttons (Add Task | Delete Selected Task | Clear Task List)
        add_task_button = QPushButton('Add a Task', clicked = lambda: self.add_task(self.task_field.text()))
        del_task_button = QPushButton('Delete Task', clicked = lambda: self.del_task(self.task_list.currentRow()))
        clear_list_button = QPushButton('Clear All Tasks', clicked = lambda: self.clear_list())
        
        # Placing Widgets into the Grid
        # Task Field is placed at (0,0), Takes up 1 row 3 cols
        window_layout.addWidget(self.task_field, 0, 0, 1, 3)

        # 3 Buttons take up 1 col and collectively 1 row, are placed in row 1
        window_layout.addWidget(add_task_button, 1, 0)
        window_layout.addWidget(del_task_button, 1, 1)
        window_layout.addWidget(clear_list_button, 1, 2)

        # Task List is placed at (2,0), Takes up 1 row and 3 cols
        window_layout.addWidget(self.task_list, 2, 0, 1, 3)

        self.show()
    
    def add_task(self, new_task):
        # Check that the new task isn't a blank field
        if new_task != '':
            self.task_list.addItem(new_task)
            self.task_field.setText('')

    def del_task(self, selected_task):
        self.task_list.takeItem(selected_task)

    def clear_list(self):
        self.task_list.clear()

if __name__ == '__main__':
    application = QApplication([])
    ex = ToDoApp()
    sys.exit(application.exec())