from Pyside6.QtCore import Slot
from Pyside6.QtWidgets import QPushButton, QWidget, QVBoxLayout
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

        self.todo_list.add_todo("a")
        self.todo_list.add_todo("b")

        self.add_todo_button.clicked.connect(self.on_button_clicked)

    @Slot()
    def on_button_clicked(self):
        self.todo_list.add_todo()
