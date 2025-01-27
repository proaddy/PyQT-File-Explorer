from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom MainWindow")

        # making menu
        menu_bar = self.menuBar()
        # File menu
        file_menu = menu_bar.addMenu("&File")
        quit_option = file_menu.addAction("Quit")
        quit_option.triggered.connect(self.quit_app)

        # Edit menu
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        # other menus
        menu_bar.addMenu("Window")
        menu_bar.addMenu("Settings")
        menu_bar.addMenu("Help")

        # working with toolbar
        tool_bar = QToolBar("My Main Toolbar")
        tool_bar.setIconSize(QSize(16, 16))
        self.addToolBar(tool_bar)

        # adding action to toolbar
        tool_bar.addAction(quit_option)

        # adding action using qaction
        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        tool_bar.addAction(action1)

        action2 = QAction(QIcon("Start.png"), "Some other action", self)
        action2.setStatusTip("Status message for some other action")
        action2.triggered.connect(self.toolbar_button_click)
        action2.setCheckable(True)
        tool_bar.addAction(action2)

        # we can separate similar tools on the toolbar
        tool_bar.addSeparator()
        tool_bar.addWidget(QPushButton("Click here"))


        # working with status bar
        self.setStatusBar(QStatusBar(self))


        button1 = QPushButton("Button1")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)
    
    # slots
    def button1_clicked(self):
        print("button 1 was clicked")

    def quit_app(self):
        self.app.quit()
    
    def toolbar_button_click(self):
        print("action1 triggered")
        self.statusBar().showMessage("Message from the app")