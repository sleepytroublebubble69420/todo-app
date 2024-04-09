from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout
from todo_list import TodoList


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.todo_list: TodoList = TodoList(self)
        self.add_todo_button: QPushButton = QPushButton(self, "+")

        layout = QVBoxLayout(self)
        self.setLayout(layout)
        layout.addWidget(self.todo_list)
        layout.addWidget(self.add_todo_button)

        self.add_todo_button.clicked.connect(self.on_button_clicked)

    @Slot()
    def on_button_clicked(self):
        self.todo_list.add_todo()
