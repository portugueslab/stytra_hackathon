from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
)

class ButtonWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button = QPushButton("Click me")
        self.state = False
        self.button.clicked.connect(
            self.change_text
        )  # here is an example of connecting Signals

        # to put widgets inside other widgets, we need layouts
        self.setLayout(QVBoxLayout())  # PyQt uses CamelCase, like C++ QT, for functions
        # properties of objects are usualy set with qobj.setProperty functions, and
        # retreived with qobj.Property() function
        self.layout().addWidget(self.button)

    # this function is connected to the clicked signal
    def change_text(self):
        if self.state:
            self.button.setText("Click me")
            self.state = False
        else:
            self.button.setText("Don't click me")
            self.state = True

if __name__ == "__main__":
    app = QApplication([])
    wb = ButtonWidget()
    wb.show()

    app.exec_()  # this starts the Qt event loop (which registers clicks, deals with signals etc)
