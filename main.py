from PySide6.QtWidgets import QApplication, QPushButton, QSlider, QWidget
import sys



from components.main_window import MainWindow
app = QApplication(sys.argv)
window = MainWindow(app)
window.show()
app.exec()


'''
# importing widgets
from components.rockwidget import RockWidget
app = QApplication(sys.argv)
window = RockWidget()
window.show()
app.exec()
'''


'''
# slider
from PySide6.QtCore import Qt
def when_slider_change(data):
    print("The value of slider currently is ", data)

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(20)
slider.setValue(8)

slider.valueChanged.connect(when_slider_change)
slider.show()
app.exec()
'''


'''
# checkbox 
def button_clicked(data):
    print("You haved clicked the button or not", data)

app = QApplication()
button = QPushButton("Check the box")
button.setCheckable(True)

button.clicked.connect(button_clicked)
button.show()
app.exec()
'''


'''
# Signal and Slots
# this is slot
def button_clicked():
    print("You clicked the button")

app = QApplication()
button = QPushButton("Click the button")

# this is signal
button.clicked.connect(button_clicked)
button.show()
app.exec()'''

'''
# importing class component
from components.button_holder import ButtonHolder
app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
app.exec()
'''

'''
# dividing the code
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