import sys
from PyQt4 import QtGui, QtCore
from functools import partial



class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Robot of EE-UBU")
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        #--------------------------------TEXT BOX-----------------------------------------------

        self.text_br = QtGui.QLineEdit(self)
        self.text_br.resize(100,25)
        self.text_br.move(70,10)
        self.text_br.setText("1000000")

        self.text_port = QtGui.QLineEdit(self)
        self.text_port.resize(100,25)
        self.text_port.move(70,40)
        self.text_port.setText("COM15")

        self.text_x = QtGui.QLineEdit(self)
        self.text_x.resize(100,25)
        self.text_x.move(70,100)
        self.text_x.setText("0")
        

        self.text_y = QtGui.QLineEdit(self)
        self.text_y.resize(100,25)
        self.text_y.move(70,140)
        self.text_y.setText("0")
        

        self.text_z = QtGui.QLineEdit(self)
        self.text_z.resize(100,25)
        self.text_z.move(70,180)
        self.text_z.setText("0")

        
        self.home()   

    def home(self):
        l1 = QtGui.QLabel(self)
        l1.setText("Buadrate :")
        l1.move(10,10)

        l2 = QtGui.QLabel(self)
        l2.setText("Comport :")
        l2.move(10,40)

        pos_x = QtGui.QLabel(self)
        pos_x.setText("X :")
        pos_x.move(50,100)

        pos_y = QtGui.QLabel(self)
        pos_y.setText("Y :")
        pos_y.move(50,140)

        pos_z = QtGui.QLabel(self)
        pos_z.setText("Z :")
        pos_z.move(50,180)

        #-----------------------------IMAGE-----------------------------------

        pic = QtGui.QLabel(self) 
        pic.setGeometry(220, 10, 238, 138)
        pixmap = QtGui.QPixmap('picture1.png')
        pic.setPixmap(pixmap)
        

        #----------------------------------------------------------------

        bar = QtGui.QProgressBar(self)
        bar.setGeometry(230,200,280,20)
       
        #---------------------------BUTTON-------------------------------------

        btn_auto = QtGui.QPushButton("Auto", self)
        btn_auto.clicked.connect(self.actions_auto)
        btn_auto.resize(250,50)
        btn_auto.move(230,230)

        btn_start = QtGui.QPushButton("Start", self)
        btn_start.clicked.connect(self.actions_manual)
        btn_start.resize(200,50)
        btn_start.move(10,230)

        btn_start = QtGui.QPushButton("Home", self)
        btn_start.clicked.connect(self.actions_home)
        btn_start.resize(100,30)
        btn_start.move(230,150)

        btn_start = QtGui.QPushButton("Ready", self)
        btn_start.clicked.connect(self.actions_ready)
        btn_start.resize(100,30)
        btn_start.move(330,150)


        self.show()
    
    #----------------------------------ACTION FUNCTIONS---------------------------
    def actions_home(self):
        buadrate = self.text_br.text()
        comport = self.text_port.text()
        print("Home Start",buadrate,comport) 

    def actions_ready(self):
        buadrate = self.text_br.text()
        comport = self.text_port.text()
        print("Ready Start",buadrate,comport) 


    def actions_auto(self):
        buadrate = self.text_br.text()
        comport = self.text_port.text()
        print("Auto Start",buadrate,comport)  

    def actions_manual(self):
        buadrate = self.text_br.text()
        comport = self.text_port.text()       
        pos_x = int(self.text_x.text())
        pos_y = int(self.text_y.text())
        pos_z = int(self.text_z.text())
        print("Manual Start",buadrate,comport,pos_x,pos_y,pos_z)  

    
        
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()