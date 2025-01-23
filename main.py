from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first mainwindow app")

button = QPushButton()
button.setText("Push me")

window.setCentralWidget(button)

window.show()
app.exec()