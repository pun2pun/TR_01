import cv2
import Arm
import pun
import time 
import chang

chang.getImage()
chang.processImage()
x,y = chang.calculateDistance()
x= x+11
y =y - 3

pun.Control('COM15',1000000,100).setReady()
pun.Control('COM15',1000000,100).Graper(27)
time.sleep(1)

Q0,Q1,Q2,Q3 = Arm.fw_kinematic(x,y,2).findPositions()
Q4,Q5,Q6,Q7 = Arm.fw_kinematic(0,20,3).findPositions()


pun.Control('COM15',1000000,100).gotoJoint(Q0,Q1,Q2,Q3,45)
time.sleep(3)
pun.Control('COM15',1000000,100).Graper(-15)
time.sleep(1)
pun.Control('COM15',1000000,100).setReady()
time.sleep(2)
pun.Control('COM15',1000000,100).gotoJoint(Q4,Q5,Q6,Q7,45)
time.sleep(3)
pun.Control('COM15',1000000,100).Graper(20)
time.sleep(1)
pun.Control('COM15',1000000,100).setReady()
time.sleep(3)
pun.Control('COM15',1000000,100).gotoHome()
time.sleep(2)