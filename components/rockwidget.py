from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout

class RockWidget(QWidget): # this class inherit qwidget
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Widget")

        button1 = QPushButton("Button1")
        button1.clicked.connect(self.button_1_click)
        button2 = QPushButton("Button2")
        button2.clicked.connect(self.button_2_click)

        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        self.setLayout(button_layout)
    
    def button_1_click(self):
        print("Button1 was clicked")
        
    def button_2_click(self):
        print("Button2 was clicked")