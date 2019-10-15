from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
)

class SimpleWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

if __name__ == "__main__":
    app = QApplication([])
    w = SimpleWidget()
    w.show()

    app.exec_()  # this starts the Qt event loop (which registers clicks, deals with signals etc)
