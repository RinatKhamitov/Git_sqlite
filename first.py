import sys, math
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPen
from random import randint
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.pushButton = QPushButton('кнопка', self)
        self.pushButton.setGeometry(280, 510, 93, 28)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.flag = True
        self.update()

    def draw(self, qp):
        R, G, B = randint(0, 255), randint(0, 255), randint(0, 255)
        pn = QPen(QColor(R, G, B))
        self.qp.setPen(pn)
        x = randint(50, 300)
        y = randint(50, 300)
        k = randint(50, 300)
        self.qp.drawEllipse(x, y, k, k)

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw(self.qp)
            self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
