from PySide6.QtWidgets import QWidget, QVBoxLayout
from todo_list import TodoList
from todo_builder import TodoBuilder


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        todo_list: TodoList = TodoList(self)
        todo_builder: TodoBuilder = TodoBuilder(self)

        layout = QVBoxLayout(self)
        self.setLayout(layout)
        layout.addWidget(todo_list)
        layout.addWidget(todo_builder)

        todo_builder.submitted.connect(todo_list.add_todo)

        self.todo_list = todo_list
        self.todo_builder = todo_builder
