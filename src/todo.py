from PySide6.QtWidgets import QListWidgetItem, QListWidget


class Todo(QListWidgetItem):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setText("Todo")
