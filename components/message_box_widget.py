from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QMessageBox

class MessageBox(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message Box")

        
        button_hard = QPushButton("hard Button")
        button_hard.clicked.connect(self.hard_button_click)
        
        button_critical = QPushButton("critical Button")
        button_critical.clicked.connect(self.critical_button_click)
        
        button_question = QPushButton("question Button")
        button_question.clicked.connect(self.question_button_click)
        
        button_information = QPushButton("information Button")
        button_information.clicked.connect(self.information_button_click)
        
        button_warning = QPushButton("warning Button")
        button_warning.clicked.connect(self.warning_button_click)
        
        button_about = QPushButton("About Button")
        button_about.clicked.connect(self.about_button_click)

        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout)

    # the hard way
    def hard_button_click(self):
        message = QMessageBox()
        message.setMinimumSize(700, 200)
        message.setWindowTitle("Message box")
        message.setText("Right went missing")
        message.setInformativeText("The something went right in life is not found (404) because nothing goes right")
        message.setIcon(QMessageBox.Warning)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)
        res = message.exec()
        if res == QMessageBox.Ok:
            print("okay was clicked")
        else:
            print("cancel was selected")


    def critical_button_click(self):
        res = QMessageBox.critical(self, "Message Title",
                                        "Critical Message",
                                        QMessageBox.Ok | QMessageBox.Cancel)
        if res == QMessageBox.Ok:
            print("Okay was clicked")
        else :
            print("okay was not clicked")
        
    def question_button_click(self):
        print("question button is clicked")

    def information_button_click(self):
        print("information button is clicked")

    def warning_button_click(self):
        print("warning button is clicked")

    def about_button_click(self):
        print("About button is clicked")