import sys
import random
from PySide6.QtWidgets import QApplication
from main_window import MainWindow

if __name__ == "__main__":
    app = QApplication([])

    main_window = MainWindow(app)
    main_window.show()

    sys.exit(app.exec())
