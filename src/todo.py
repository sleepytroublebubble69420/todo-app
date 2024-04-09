from PySide6.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QLabel
from PySide6.QtCore import Slot


class Todo(QWidget):
    def __init__(self, label = "Todo", parent = None):
        super().__init__(parent)

        layout: QHBoxLayout = QHBoxLayout()
        self.setLayout(layout)

        self.label: QLabel = QLabel(label)
        layout.addWidget(self.label)

        self.check_box: QCheckBox = QCheckBox()
        layout.addWidget(self.check_box)
        self.check_box.stateChanged.connect(self.on_box_checked)

    @Slot()
    def on_box_checked(self, state):
        print(self.label.text())
        print(state)
