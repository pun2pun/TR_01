import sys
from PyQt4 import QtGui, QtCore
from functools import partial
import pun
import punAuto
import Arm
import readCSV


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 600, 300)
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
        self.text_port.setText("COM4")

        self.text_speed = QtGui.QLineEdit(self)
        self.text_speed.resize(100,25)
        self.text_speed.move(70,70)
        self.text_speed.setText("25")

        self.text_x = QtGui.QLineEdit(self)
        self.text_x.resize(100,25)
        self.text_x.move(70,120)
        self.text_x.setText("0")
        

        self.text_y = QtGui.QLineEdit(self)
        self.text_y.resize(100,25)
        self.text_y.move(70,150)
        self.text_y.setText("0")
        

        self.text_z = QtGui.QLineEdit(self)
        self.text_z.resize(100,25)
        self.text_z.move(70,180)
        self.text_z.setText("0")

        self.text_rt = QtGui.QLineEdit(self)
        self.text_rt.resize(75,25)
        self.text_rt.move(470,130)
        self.text_rt.setText("170 to -170")

        
        self.home()   

    def home(self):
        l1 = QtGui.QLabel(self)
        l1.setText("Buadrate :")
        l1.move(10,10)

        l2 = QtGui.QLabel(self)
        l2.setText("Comport :")
        l2.move(10,40)

        l3 = QtGui.QLabel(self)
        l3.setText("Speed(%) :")
        l3.move(10,70)

        pos_x = QtGui.QLabel(self)
        pos_x.setText("X :")
        pos_x.move(50,120)

        pos_y = QtGui.QLabel(self)
        pos_y.setText("Y :")
        pos_y.move(50,150)

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

        btn_auto = QtGui.QPushButton("Auto \ncolor", self)
        btn_auto.clicked.connect(self.actions_auto)
        btn_auto.resize(120,50)
        btn_auto.move(230,230)


        btn_auto = QtGui.QPushButton("Auto \ntype", self)
        btn_auto.clicked.connect(self.actions_auto)
        btn_auto.resize(120,50)
        btn_auto.move(360,230)

        btn_start = QtGui.QPushButton("Go to point", self)
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

        btn_start = QtGui.QPushButton("Grap", self)
        btn_start.clicked.connect(self.actions_grap)
        btn_start.resize(100,30)
        btn_start.move(460,10)

        
        btn_start = QtGui.QPushButton("unGrap", self)
        btn_start.clicked.connect(self.actions_ungrap)
        btn_start.resize(100,30)
        btn_start.move(460,40)

        btn_start = QtGui.QPushButton("Rotate Hand", self)
        btn_start.clicked.connect(self.actions_rotate_hand)
        btn_start.resize(100,30)
        btn_start.move(460,100)


        self.show()
    
    #----------------------------------ACTION FUNCTIONS---------------------------
    def actions_home(self):
        buadrate = self.text_br.text()
        comport = self.text_port.text()
        speed = self.text_speed.text()
        speed = int((int(speed) / 100) * 255)
        if(speed >255):speed = 255
        pun.Control(comport,buadrate,speed).gotoHome()
        print("Home Start",buadrate,comport) 

    def actions_rotate_hand(self):
        angle = int(self.text_rt.text())
        buadrate = self.text_br.text()
        comport = self.text_port.text()
        speed = self.text_speed.text()
        speed = int((int(speed) / 100) * 255)
        if(speed >255):speed = 255
        pun.Control(comport,buadrate,speed).Rotate_hnad(angle)
        print("grap Start",buadrate,comport) 

    def actions_grap(self):
        buadrate = self.text_br.text()
        comport = self.text_port.text()
        speed = self.text_speed.text()
        speed = int((int(speed) / 100) * 255)
        if(speed >255):speed = 255
        pun.Control(comport,buadrate,speed).Graper(-15)
        print("grap Start",buadrate,comport) 

    def actions_ungrap(self):
        buadrate = self.text_br.text()
        comport = self.text_port.text()
        speed = self.text_speed.text()
        speed = int((int(speed) / 100) * 255)
        if(speed >255):speed = 255
        pun.Control(comport,buadrate,speed).Graper(20)
        print("grap Start",buadrate,comport) 

    def actions_ready(self):
        buadrate = self.text_br.text()
        comport = self.text_port.text()
        speed = self.text_speed.text()
        speed = int((int(speed) / 100) * 255)
        if(speed >255):speed = 255
        pun.Control(comport,buadrate,speed).setReady()
        print("Ready Start",buadrate,comport) 


    def actions_auto(self):
        buadrate = self.text_br.text()
        comport = self.text_port.text()
        speed = self.text_speed.text()
        speed = int((int(speed) / 100) * 255)
        if(speed >255):speed = 255 
        punAuto.conecting_robot(comport,buadrate).run()
        print("Auto Start",buadrate,comport)  

    def actions_manual(self):
        angle = int(self.text_rt.text())
        buadrate = self.text_br.text()
        comport = self.text_port.text() 
        speed = self.text_speed.text()
        speed = int((int(speed) / 100) * 255)
        if(speed >255):speed = 255
        pos_x = int(self.text_x.text())
        
        pos_y = int(self.text_y.text())
        pos_z = int(self.text_z.text())

        x = readCSV.getPositons(pos_x,pos_y,pos_z)
        pun.Control(comport,buadrate,speed).gotoJoint(x[0],x[1],x[2],x[3],angle)
        
        print("Manual Start",buadrate,comport,pos_x,pos_y,pos_z)  

    
        
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()