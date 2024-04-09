from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Slot


class Todo(QWidget):
    def __init__(self, label = "Todo", parent = None):
        super().__init__(parent)

        layout: QHBoxLayout = QHBoxLayout()
        self.setLayout(layout)

        self.label: QLabel = QLabel(label)
        layout.addWidget(self.label)

        self.button: QPushButton = QPushButton()
        layout.addWidget(self.button)
        self.button.clicked.connect(self.on_button_clicked)

    @Slot()
    def on_button_clicked(self):
        print(self.label.text())
