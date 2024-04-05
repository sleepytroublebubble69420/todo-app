from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()

        self.app: QApplication = app
        self.setLayout(QHBoxLayout(self))

        self.button1: QPushButton = QPushButton("Push me", self)
        button: QPushButton = self.button1
        button.setFixedSize(100, 60)
        self.setCentralWidget(button)

        self.button2: QPushButton = QPushButton("Push me", self)
        button: QPushButton = self.button2
        button.setFixedSize(100, 60)
        self.setCentralWidget(button)

        self.button3: QPushButton = QPushButton("Push me", self)
        button: QPushButton = self.button3
        button.setFixedSize(100, 60)
        self.setCentralWidget(button)
