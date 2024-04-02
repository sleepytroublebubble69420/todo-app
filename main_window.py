import sys
from PySide6.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()

        self.app: QApplication = app
