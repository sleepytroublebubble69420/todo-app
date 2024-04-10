from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLineEdit, QPushButton, QWidget, QHBoxLayout


class TodoBuilder(QWidget):
    submitted: Signal = Signal()

    def __init__(self, parent=None):
        super().__init__()

        layout: QHBoxLayout = QHBoxLayout(self)
        self.setLayout(layout)

        line_edit: QLineEdit = QLineEdit("Todo", self)
        button: QPushButton = QPushButton(self)

        layout.addWidget(line_edit)
        layout.addWidget(button)

        line_edit.returnPressed.connect(button.clicked)
        button.clicked.connect(self.submitted.emit)
