from threading import Thread
import cv2
import Arm
import pun
import chang
import time

speed = 80
buarate = 1000000
global result,coordinate,number_objects,COLOR_s,f_grap
result = False
coordinate = []
COLOR_s =  []

size = 5
f_grap = 0.4405*(size**2) + (1.775*size) - 42.06

def init():
	pun.Control('COM4',buarate,speed).gotoHome()

		
	objects = chang.getImage()
	number_objects = len(objects)
	print(number_objects)

	

	
	for i in range(number_objects):

		positions_x = objects[i][1]
		positions_y = objects[i][0]
		color = objects[i][2]  
		x = ( positions_x / 10 )+12
		y = (( positions_y *-1) /10 ) +25.6

		z = 2
		y=y-5

		x = Arm.fw_kinemtic(x,y,z).findPositions()
		coordinate.append((x))
		COLOR_s.append(color)
	
	



def Check():
	chang.getImage_respons()
	check_ob = cv2.imread('data/Respons.jpg')
	b,g,r = check_ob[33,192] 
	sum_color = (b+g+r) / 3
	print(b,g,r,sum_color)
	if( (b%sum_color) > 10 or (b%sum_color) < 10 ):
		result = False
	else:
		result = True
	print(result)
	return result




def robotic_work():
	init()
	number_objects = len(coordinate)
	print(number_objects,coordinate)
	for rounds in range(number_objects):
		x = coordinate[rounds]
		color = COLOR_s[rounds]

		pun.Control('COM4',buarate,speed).Graper(40)
		time.sleep(1)
		pun.Control('COM4',buarate,speed).setReady()
		time.sleep(1)
		pun.Control('COM4',buarate,speed).gotoJoint(x[0],x[1],x[2],x[3],45)
		time.sleep(2)

		
		pun.Control('COM4',buarate,speed).Graper(f_grap)
		time.sleep(2)
		
		pun.Control('COM4',buarate,speed).setReady()
		time.sleep(2)

		
		
						   

		if( color == 'Green'):pun.Control('COM4',buarate,speed).gotoJoint(90,5,-55,-90,45)
		if( color == 'Red'):pun.Control('COM4',buarate,speed).gotoJoint(-90,5,-55,-90,45)

		time.sleep(2)
		pun.Control('COM4',buarate,speed).Graper(15)
		time.sleep(2)
		pun.Control('COM4',buarate,speed).setReady()
		time.sleep(1)




t1 = Thread	(target=chang.getImage)
t2 = Thread	(target=robotic_work)

while True:
	print(result)
	if(result == True):
		break
	else:
		t2.start()	

