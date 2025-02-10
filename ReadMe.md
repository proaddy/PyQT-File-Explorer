Simply run the FileExplorer.py file


## Qt
[PySide6 Documentation](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/).

Qt originally a cpp library to make GUI not used for python, it can make resuable code for any platform as it's precompiler but can be recompiled for any other platform.
Making it platform independent.

Making GUIs are good but we should always organize as we handle more and more code
In the main.py file we have written three methods to write the Qt application and the last method is the more organized way as it helps to make it resuable and even easy to make update without breaking anything.

# Qt Starting
## PySide6 
A python library which uses Qt at it's core

### PySide6.QtWidgets 
From here we import all the things we need to build our application

#### QApplication
this is used to start the eventloop for the program and also handles all the events such as click, edit, type, keypresses, etc.

#### QMainWindow, QPushButton
Mainwindow and pushbutton are the widgets. main windows is the window which contains the minimize, maximize, close button, toolbar, statusbar, and menu.
Where as pushbutton is just a button you can give it height, and width, and change the text.

QPushButton was derived from the Parent class QAbstractButton.

### Signal and Slots
it's like a eventlistener once a button it pressed it gives signal to the events litening for that button press and the event is triggered.

when a button is pressed it sends a signal but to see what kind of signal we have to check the parent class which is QAbstractButton.
#### QAbstractButton
This is the abstract from which multiple types of buttons are derived such as radioButton, checkbox and toolbutton
slots and signals are available to see.

It has signals such as clicked, pressed, released, toggled
clicked will let us know it's the button was clicked
Pressed means the button was presses and still holding
released means the button which was holded down is let go
and toggled it checkbox and we can pass true and false data if it's checked or not.

#### QSlider
can set maximum and minimum value, and a default value
mention if it's horizontal or vertical (maybe)

And the signal can be monitored if it's changed different from button