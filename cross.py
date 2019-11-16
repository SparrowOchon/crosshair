import sys
import signal
from PyQt5 import QtCore, QtGui, QtWidgets


class Crosshair(QtWidgets.QWidget):
    def __init__(self, parent=None, windowSize=24, penWidth=5):
        QtWidgets.QWidget.__init__(self, parent)
        self.ws = windowSize
        self.resize(windowSize + 1, windowSize + 1)
        self.pen = QtGui.QPen(QtGui.QColor(0, 128, 128, 80))
        self.pen.setWidth(penWidth)
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint
            | QtCore.Qt.WindowStaysOnTopHint
            | QtCore.Qt.WindowTransparentForInput
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.move(
            QtWidgets.QApplication.desktop().screen().rect().center()
            - self.rect().center()
            + QtCore.QPoint(1, 231)
        )

    def paintEvent(self, event):
        ws = self.ws
        d = 6
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        # painter.drawLine( x1,y1, x2,y2    )
        painter.drawPoint(ws / 2, ws / 2)
        # painter.drawLine(ws / 2, 0, ws / 2, ws / 2 - ws / d)  # Top
        # painter.drawLine(ws / 2, ws / 2 + ws / d, ws / 2, ws)  # Bottom
        # painter.drawLine(0, ws / 2, ws / 2 - ws / d, ws / 2)  # Left
        # painter.drawLine(ws / 2 + ws / d, ws / 2, ws, ws / 2)  # Right


signal.signal(signal.SIGINT, signal.SIG_DFL)
app = QtWidgets.QApplication([])

widget = Crosshair(windowSize=25, penWidth=5)
widget.show()
app.exec_()
