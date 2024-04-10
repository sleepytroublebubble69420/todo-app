from PySide6.QtWidgets import QListWidget, QListWidgetItem
from todo import Todo


class TodoList(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def add_todo(self, label: str = None):
        item: QListWidgetItem = QListWidgetItem()
        self.addItem(item)

        todo: Todo = Todo(label)
        item.setSizeHint(todo.minimumSizeHint())
        self.setItemWidget(item, todo)
        todo.button.clicked.connect(lambda: self.remove_todo(item))

    def remove_todo(self, item: QListWidget):
        self.takeItem(self.row(item))
