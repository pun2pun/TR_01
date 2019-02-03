from pyax12.connection import Connection
import time


class Control:
    def __init__(self,comPort,Buadrate,sp):
        self.motor_1 = 7
        self.motor_2 = 11
        self.motor_3 = 3
        self.motor_4 = 13
        self.motor_5 = 15
        self.motor_6 = 18
        self.port = comPort
        self.bps = Buadrate
        self.speed = sp


    def gotoHome(self):

        robot = Connection(port=self.port, baudrate=self.bps)

        robot.goto(self.motor_5, 45, speed=self.speed+20, degrees=True)
        time.sleep(1.5)
        robot.goto(self.motor_6,0, speed=self.speed, degrees=True)      
        robot.goto(self.motor_3,-130, speed=self.speed, degrees=True)
        robot.goto(self.motor_2,-90, speed=self.speed, degrees=True)
        time.sleep(3)
        robot.goto(self.motor_1,-90, speed=self.speed, degrees=True)
        time.sleep(1)
        robot.goto(self.motor_4, -90, speed=self.speed, degrees=True) 
        robot.close()  
    
    def gotoJoint(self,p1,p2,p3,p4,p5):

        robot = Connection(port=self.port, baudrate=self.bps)
 
        time.sleep(0.5)
        robot.goto(self.motor_1,p1, speed=self.speed, degrees=True)
        robot.goto(self.motor_2,p2, speed=self.speed, degrees=True)
        robot.goto(self.motor_3,p3, speed=self.speed, degrees=True)
        robot.goto(self.motor_4,p4, speed=self.speed, degrees=True)
        robot.goto(self.motor_5,p5, speed=self.speed, degrees=True)
        time.sleep(0.5)
        robot.close() 
        
    def setReady(self):

        robot = Connection(port=self.port, baudrate=self.bps)
 
        time.sleep(0.5)
        robot.goto(self.motor_2,-60, speed=self.speed, degrees=True)
        time.sleep(1.5)
        robot.goto(self.motor_1,0, speed=self.speed, degrees=True)
        robot.goto(self.motor_3,-90, speed=self.speed, degrees=True)
        robot.goto(self.motor_4,-90, speed=self.speed, degrees=True)
        robot.goto(self.motor_5,45, speed=self.speed, degrees=True)
        time.sleep(0.5)
        robot.close() 

      
    def Graper(self,p6):

        robot = Connection(port=self.port, baudrate=self.bps)
        robot.goto(self.motor_6, p6, speed=self.speed, degrees=True)
        robot.close() 
