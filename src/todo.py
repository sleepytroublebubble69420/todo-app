from PySide6.QtWidgets import QWidget, QHBoxLayout, QCheckBox


class Todo(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        layout: QHBoxLayout = QHBoxLayout()
        self.setLayout(layout)
        layout.addWidget(QCheckBox())
