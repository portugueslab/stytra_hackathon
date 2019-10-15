from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QSlider,
    QHBoxLayout,
    QPushButton,
)
import pyqtgraph as pg
import numpy as np


class SimpleWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass


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
        )  # they are emmited with the emit function


class BigExample(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slider_freq = QSlider()
        self.plot = pg.PlotWidget()
        self.plot_line = pg.PlotCurveItem()
        self.plot.addItem(self.plot_line)

        self.slider_freq.valueChanged.connect(self.update_plot)

        self.setLayout(QHBoxLayout())
        self.setWindowTitle("Plots")
        self.layout().addWidget(self.slider_freq)
        self.layout().addWidget(self.plot)

        self.xdata = np.linspace(0, 1, 1000)

    def update_plot(self):
        self.plot_line.setData(
            x=self.xdata, y=np.sin(self.xdata * self.slider_freq.value() / 20)
        )


if __name__ == "__main__":
    app = QApplication([])
    w = SimpleWidget()
    w.show()

    wb = ButtonWidget()
    wb.show()

    sv = SignalButtonWidget()
    sv.sigPushed.connect(wb.change_text)
    sv.show()

    pw = BigExample()
    pw.show()

    app.exec_()  # this starts the Qt event loop (which registers clicks, deals with signals etc)
