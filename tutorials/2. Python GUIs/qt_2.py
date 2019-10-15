from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
)



class ButtonWidget(QWidget):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button = QPushButton("Click me")
        self.state = False
        self.button.clicked.connect(
            self.change_text
        )  # here is an example of connecting Signals
        self.app = app

        # to put widgets inside other widgets, we need layouts
        self.setLayout(QVBoxLayout())  # PyQt uses CamelCase, like C++ QT, for functions
        # properties of objects are usualy set with qobj.setProperty functions, and
        # retreived with qobj.Property() function
        self.layout().addWidget(self.button)

    # this function is connected to the clicked signal
    def change_text(self):
        print(self.button.text())
        if self.state:
            self.button.setText("Click me")
            self.state = False

        else:
            self.button.setText("Don't click me")
            self.state = True






class SignalButtonWidget(QWidget):
    sigPushed = pyqtSignal()  # this is how we specify our own signals

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button = QPushButton("Emit signal")
        self.setLayout(QVBoxLayout())
        self.setWindowTitle("Signal emitting window")
        self.layout().addWidget(self.button)
        self.button.clicked.connect(
            self.sigPushed.emit
        )  # they are emitted with the emit function
        self.state = True

    # this function will be connected to the custom signal
    def change_text(self):
        if self.state:
            self.button.setText("Emit signal 1")
            self.state = False

        else:
            self.button.setText("Emit signal 0")
            self.state = True



if __name__ == "__main__":
    app = QApplication([])

    wb = ButtonWidget(app=app)
    sw = SignalButtonWidget()

    sw.sigPushed.connect(sw.change_text)

    # Combine the two widgets in one:
    combined_widget = QWidget()
    combined_layout = QVBoxLayout()
    [combined_layout.addWidget(w) for w in [wb, sw]]
    combined_widget.setLayout(combined_layout)
    combined_widget.show()



    app.exec_()  # this starts the Qt event loop (which registers clicks, deals with signals etc)
