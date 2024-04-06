import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from todo_list import TodoList
from todo import Todo


def main():
    app = QApplication([])

    main_window: MainWindow = MainWindow(app)

    todo_list: TodoList = TodoList(main_window)
    main_window.setCentralWidget(todo_list)

    todo1: Todo = Todo()
    todo_list.addItem(todo1)

    main_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
