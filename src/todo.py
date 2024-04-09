from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Signal


class Todo(QWidget):
    clicked: Signal = Signal()

    def __init__(self, label = "Todo", parent = None):
        super().__init__(parent)

        layout: QHBoxLayout = QHBoxLayout()
        self.setLayout(layout)

        label: QLabel = QLabel(label)
        layout.addWidget(label, 9)

        self.button: QPushButton = QPushButton()
        layout.addWidget(self.button, 1)
