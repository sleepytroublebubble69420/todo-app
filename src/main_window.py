from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton


class MainWindow(QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()

        self.app: QApplication = app

        self.button: QPushButton = QPushButton("Push me", self)
        button: QPushButton = self.button
        button.released.connect(self.print_txt)
        self.setCentralWidget(button)

    @Slot()
    def print_txt(self):
        print("Slot")
