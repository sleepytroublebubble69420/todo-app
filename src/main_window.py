from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, QWidget
from todo_list import TodoList


class MainWindow(QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()

        self.app: QApplication = app
        centralWidget: TodoList = TodoList(self)
        self.setCentralWidget(centralWidget)
