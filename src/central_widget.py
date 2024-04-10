from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout
from todo_list import TodoList
from todo_builder import TodoBuilder


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.todo_list: TodoList = TodoList(self)
        todo_builder: TodoBuilder = TodoBuilder(self)

        layout = QVBoxLayout(self)
        self.setLayout(layout)
        layout.addWidget(self.todo_list)
        layout.addWidget(todo_builder)

        todo_builder.submitted.connect(self.todo_list.add_todo)
