
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QComboBox, QDialog, QDialogButtonBox, QFormLayout,
                             QGridLayout, QGroupBox, QHBoxLayout, QLabel, QPushButton,
                             QVBoxLayout, QRadioButton)
from PyQt5.QtGui import (QIcon, QPixmap, QPainter, QColor, QPen)
from PyQt5.QtCore import (pyqtSlot, Qt, QTimeLine, QPropertyAnimation, pyqtProperty)

import json
from pprint import pprint


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ajust Labels'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

        self.dataArr = ['../darkflow/sample_img/out/beatles.json',
                        '../darkflow/sample_img/out/uhack.json']
        self.data = json.load(open(self.dataArr[0]))
        self.numElement = len(self.data)
        self.count = 0
        self.fileCount = 0


        self.px = self.data[self.count]["topleft"]["x"]
        self.py = self.data[self.count]["topleft"]["y"]
        self.pw = self.data[self.count]["bottomright"]["x"] - self.data[self.count]["topleft"]["x"]
        self.ph = self.data[self.count]["bottomright"]["y"] - self.data[self.count]["topleft"]["y"]

        self.pics = ['../darkflow/sample_img/beatles.jpg',
                     '../darkflow/sample_img/uhack.jpg']
        self.numPics = len(self.pics)
        self.picPath = self.pics[self.fileCount]

        self.initUI()

    def initUI(self):

        # radio buttons
        box = QGroupBox("Object", self)
        box.resize(200, 550)
        box.move(650, 0)

        layout = QGridLayout()
        layout.addWidget(QRadioButton("Car"))
        layout.addWidget(QRadioButton("Person"))
        layout.addWidget(QRadioButton("Other"))

        box.setLayout(layout)

        # OK button
        button = QPushButton('OK', self)
        # button.setToolTip('myButton') #??? what is tooltip
        button.move(700,500)
        button.clicked.connect(lambda: self.OKButtonPressed())

        self.show()

    # TODO: output xml
    #def radioButtonPressed:
        #self.update(self, '../cam001_1.jpg', 10, 10, self.rect().width() - 10, 10)

    #@pyqtSlot() #??? not working
    def OKButtonPressed(self):

        if self.count < self.numElement - 1 and self.fileCount < self.numPics:
            self.count = self.count + 1

        else:
            if self.fileCount < self.numPics:
                self.fileCount = self.fileCount + 1
                if (self.fileCount >=  self.numPics):
                    sys.exit(0)
                self.data = json.load(open(self.dataArr[self.fileCount]))
                self.numElement = len(self.data)
                self.picPath = self.pics[self.fileCount]
                self.count = 0




        self.px = self.data[self.count]["topleft"]["x"]
        self.py = self.data[self.count]["topleft"]["y"]
        self.pw = self.data[self.count]["bottomright"]["x"] - self.data[self.count]["topleft"]["x"]
        self.ph = self.data[self.count]["bottomright"]["y"] - self.data[self.count]["topleft"]["y"]

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(self.picPath)
        painter.drawPixmap(pixmap.rect(), pixmap)
        pen = QPen(Qt.red, 3)
        painter.setPen(pen)
        painter.drawRect(self.px, self.py, self.pw, self.ph)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


