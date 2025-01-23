from PySide6.QtWidgets import QMainWindow, QPushButton
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button holder")
        button = QPushButton("Press me")

        # button as central widget
        self.setCentralWidget(button)