import sys
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget

class Button(QWidget):

    clicked = Signal(Qt.MouseButton)

    def mousePressEvent(self, event):
        self.clicked.emit(event.button())

def function():
    print("The 'function' has been called!")

app = QApplication()
button = QPushButton("Call function")
button.clicked.connect(function)
button.show()
sys.exit(app.exec())
