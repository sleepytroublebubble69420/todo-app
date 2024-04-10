from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QLineEdit, QPushButton, QWidget, QHBoxLayout


class TodoBuilder(QWidget):
    submitted: Signal = Signal(str)

    def __init__(self, parent=None):
        super().__init__()

        layout: QHBoxLayout = QHBoxLayout(self)
        self.setLayout(layout)

        self.line_edit: QLineEdit = QLineEdit("Todo", self)
        button: QPushButton = QPushButton(self)

        layout.addWidget(self.line_edit)
        layout.addWidget(button)

        self.line_edit.returnPressed.connect(button.clicked)
        button.clicked.connect(self.submit_todo)

    @Slot()
    def submit_todo(self):
        todo_label = self.line_edit.text()
        self.submitted.emit(todo_label)
