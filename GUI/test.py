
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QComboBox, QDialog, QDialogButtonBox, QFormLayout,
                             QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMenu, QMenuBar, QPushButton,
                             QSpinBox, QTextEdit, QVBoxLayout, QRadioButton)
from PyQt5.QtGui import (QIcon, QPixmap, QPainter, QColor, QPen)
from PyQt5.QtCore import (pyqtSlot, Qt, QTimeLine, QPropertyAnimation, pyqtProperty)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image'
        self.left = 10
        self.top = 10
        self.width = 900 #640
        self.height = 600 #480
        self.initUI()

        '''
        super(Dialog, self).__init__()
        button=QPushButton("click")
        button.clicked.connect(self.slot_method) # signal connects to slot

        mainLayout=QVBoxLayout()
        mainLayout.addWidget(button)

        self.setLayout(mainLayout)
        self.setWindowTitle("Button Example - pythonspot.com")
        '''

    def initUI(self):

        #self.statusBar().showMessage('myMessage')

        # Create widget for image
        '''
        label = QLabel(self)
        pixmap = QPixmap('../cam001_1.jpg')
        label.setPixmap(pixmap)
        #label.resize(pixmap.width(), pixmap.height())
        '''
        # Create widget for options
        box = QGroupBox("Object", self)
        box.resize(200, 550)
        box.move(650, 0)

        layout = QGridLayout()
        #layout.setColumnStretch(1, 4)
        #layout.setColumnStretch(2, 4)
        #layout.move(800,500)
        layout.addWidget(QRadioButton("Car"))
        layout.addWidget(QRadioButton("Person"))
        layout.addWidget(QRadioButton("Bike"))

        box.setLayout(layout)

        # add paint widget
        self.m = PaintWidget(self, picPath, bx, by, bw, bh)
        self.m.move(0,50)
        self.m.resize(600, 400)

        self.show()

    #def radioButtonPressed:


    #def nextButtonPressed:



class PaintWidget(QWidget, picPath, bx, by, bw, bh):
    def __init__(self):
        super().__init__()
        self.picPath = ''
        self.left = 0
        self.top = 0
        self.width = 0
        self.height = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(picPath)
        painter.drawPixmap(self.rect(), pixmap)
        pen = QPen(Qt.red, 3)
        painter.setPen(pen)
        painter.drawRect(bx, by, bw, bh)

        '''
        button = QPushButton('PyQt5 button', self)
        # button.setToolTip('myButton') #??? what is tooltip
        button.move(100,70)
        button.clicked.connect(self.on_click)
        '''


'''
class PaintWidget(QWidget):
    def painEvent(self, event):
        qp = QPainter(self)
        #qp.begin(self)
        qp.setPen(Qt.red)
        #qp.setBrush(Qt.red)
        qp.drawRect(self, 100, 200, 300, 400)
        #qp.end()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


