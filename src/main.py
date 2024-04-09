import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from central_widget import CentralWidget


def main():
    app = QApplication([])

    main_window: MainWindow = MainWindow(app)

    central_widget = CentralWidget(main_window)
    main_window.setCentralWidget(central_widget)

    main_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
