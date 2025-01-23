
# Importing the components
from PySide6.QtWidgets import QApplication, QWidget

# Module responsible for processing cmd arguments
import sys

# creating application handles: running, click events and etc.
app = QApplication(sys.argv)

# making widget
window = QWidget()

# shows widget on the panel
window.show()

# start the event loop
app.exec()