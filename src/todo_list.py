from PySide6.QtWidgets import QListWidget


class TodoList(QListWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
