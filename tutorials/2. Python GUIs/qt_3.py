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


class BigExample(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slider_freq = QSlider()  # Create a slider
        self.plot = pg.PlotWidget()  # Create a plot
        self.plot_line = pg.PlotCurveItem()  # Create a plot line
        self.plot.addItem(self.plot_line)  # Add line to plot

        # Connect valueChanged signal from slider to plot update function:
        self.slider_freq.valueChanged.connect(self.update_plot)

        # Set a layout and add the widgets:
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

    pw = BigExample()
    pw.show()

    app.exec_()  # this starts the Qt event loop (which registers clicks, deals with signals etc)
