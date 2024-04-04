import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow


def main():
    app = QApplication([])

    main_window = MainWindow(app)
    main_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
