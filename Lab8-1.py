import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle('Simple Drawing')
        self.rabbit = QPixmap('rabbit.png')

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
 
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
 
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(240, 255, 0))
        p.drawPie(50, 150, 100, 100, 0, 320 * 16)
        
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle('Simple Drawing')
        self.rabbit = QPixmap('rabbit.png')

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint( 70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
        ])

        p.setPen(QColor(255, 0, 0 ))
        p.setBrush(QColor(255, 0, 0 ))
        p.drawPie(50, 150, 100, 100, 0, 360 * 16)
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

class Simple_drawing_window3(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle('Simple Drawing')
        self.rabbit = QPixmap('rabbit.png')


    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(170, 25, 202 ))

        points = QPolygon([
            QPoint(10, 10),
            QPoint(10, 100),
            QPoint(100, 10),
            QPoint(100, 100)
 
        ])
 
        p.drawPolygon(points)
        
 
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
  

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window1()
    w2 = Simple_drawing_window2()
    w3 = Simple_drawing_window3()
    w.show()
    w2.show()
    w3.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())