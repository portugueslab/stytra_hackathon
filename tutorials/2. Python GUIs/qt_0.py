from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
)

class SimpleWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("my first window")


app = QApplication([])
w = SimpleWidget()
w.show()
app.exec()  # this starts the Qt event loop (which registers clicks, deals with signals etc)
print("Here we are")