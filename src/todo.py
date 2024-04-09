from PySide6.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QLineEdit
from PySide6.QtCore import Slot


class Todo(QWidget):
    def __init__(self, todo_name = "Todo", parent = None):
        super().__init__(parent)

        layout: QHBoxLayout = QHBoxLayout()
        self.setLayout(layout)

        self.todo_name: QLineEdit = QLineEdit(todo_name)
        layout.addWidget(self.todo_name)

        self.check_box: QCheckBox = QCheckBox()
        layout.addWidget(self.check_box)
        self.check_box.stateChanged.connect(self.on_box_checked)

    @Slot()
    def on_box_checked(self, state):
        print(self.todo_name.text())
        print(state)
