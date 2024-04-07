import sys
from PySide6.QtWidgets import QApplication, QListWidgetItem
from main_window import MainWindow
from todo_list import TodoList
from todo import Todo


def main():
    app = QApplication([])

    main_window: MainWindow = MainWindow(app)

    todo_list: TodoList = TodoList(main_window)
    main_window.setCentralWidget(todo_list)

    item: QListWidgetItem = QListWidgetItem("testasrtieansotienastenaston")
    todo_list.addItem(item)
    todo1: Todo = Todo()
    item.setSizeHint(todo1.minimumSizeHint())
    todo_list.setItemWidget(item, todo1)

    main_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
