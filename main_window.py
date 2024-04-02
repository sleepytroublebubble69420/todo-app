import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton

class MainWindow(QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()

        self.app: QApplication = app

        self.button = QPushButton("Push me", self)
        self.button.released.connect(self.print_txt)
        self.setCentralWidget(self.button)

    @Slot()
    def print_txt(self):
        print("Slot")
