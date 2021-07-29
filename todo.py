from PyQt6.QtGui import QFont
from PyQt6 import QtCore, QtWidgets, QtGui
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

    def initUI(self, window_title: str, window_x: int, window_y: int, window_width: int, window_height: int):
        '''Sets up the main UI window'''
        # Setting up the Window
        self.setWindowTitle(window_title)
        self.setGeometry(window_x, window_y, window_width, window_height)
        self.setWindowIcon(QtGui.QIcon('images/check_mark.jpg'))

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

        self.update_existing_tasks()

        self.show()
    
    def add_task(self, new_task: str):
        '''Adds a task into the app, also stores it into task_data.txt'''

        # Check that the new task isn't a blank field, updates task_field list
        if new_task != '':
            self.task_list.addItem(new_task)
            self.task_field.setText('')

            # Stores the new task in task_data.txt
            self.file_append_value(new_task)

    def del_task(self, selected_task_row: int):
        '''Deletes a task from the task list, also deletes it from task_data.txt'''

        # Store name of the task to be deleted first
        deleted_task_name = self.task_list.item(selected_task_row).text()

        # Delete the task from task_data.txt
        self.file_delete_value(deleted_task_name)

        # Delete task from UI
        self.task_list.takeItem(selected_task_row)

    def clear_list(self):
        '''Clears all tasks from task list, also deletes everything in task_data.txt'''

        self.task_list.clear()

        open('task_data.txt', 'w').close()

    def update_existing_tasks(self):
        '''Checks the task_data.txt file and updates the list widget with the tasks'''

        file_lines = self.get_lines()
        if len(file_lines) > 0:
            for line in file_lines:
                self.task_list.addItem(line.strip('\n'))

    def file_delete_value(self, task_name : str):
        '''Given a string, deletes the corresponding string in the task_data.txt file'''

        file_lines = self.get_lines()
        
        with open('task_data.txt', 'w') as task_file:
            for line in file_lines:
                if line.strip('\n') != task_name:
                    task_file.write(line)

    def file_append_value(self, task_name : str):
        '''Given a string, appends the string to task_data.txt file'''

        with open('task_data.txt', 'a') as task_file:
            task_file.write(task_name + '\n')

    def get_lines(self) -> list:
        '''Gets the lines within task_data.txt'''
        with open ('task_data.txt', 'r') as task_file:
            file_lines = task_file.readlines()
        
        return file_lines

        
    

if __name__ == '__main__':
    application = QApplication([])
    ex = ToDoApp()
    sys.exit(application.exec())