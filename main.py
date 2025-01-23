from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button holder")
        button = QPushButton("Press me")

        # button as central widget
        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
app.exec()




'''
# contains only global scope 
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first mainwindow app")

button = QPushButton()
button.setText("Push me")

window.setCentralWidget(button)

window.show()
app.exec()
'''