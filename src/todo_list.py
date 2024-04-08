from PySide6.QtWidgets import QListWidget, QListWidgetItem
from todo import Todo


class TodoList(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def add_todo(self, label=None):
        item: QListWidgetItem = QListWidgetItem()
        self.addItem(item)
        todo1: Todo = Todo(label)
        item.setSizeHint(todo1.minimumSizeHint())
        self.setItemWidget(item, todo1)
