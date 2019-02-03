import Arm
import pun
import chang
import time
speed = 80
buarate = 1000000
'''
chang.getImage()
positions = chang.processImage_2()

speed = 90
buarate = 1000000

x = ( positions[0] / 10 )+9
y = (( positions[1] *-1) /10 ) + 26.75
color_green = positions[2]
color_red = positions[3]

size = (positions[4] -1 )/10

f_grap = 0.4405*(size**2) + (1.775*size) - 42.06

print(f_grap)


pun.Control('COM4',buarate,speed).setReady()
pun.Control('COM4',buarate,speed).Graper(27)

z = 2

y=y-5

x = Arm.fw_kinemtic(x+2,y,z).findPositions()



pun.Control('COM4',buarate,speed).Graper(40)
time.sleep(2)
pun.Control('COM4',buarate,speed).setReady()
time.sleep(2)
pun.Control('COM4',buarate,speed).gotoJoint(x[0],x[1],x[2],x[3],45)
time.sleep(2)
pun.Control('COM4',buarate,speed).Graper(f_grap)
time.sleep(2)
pun.Control('COM4',buarate,speed).setReady()
time.sleep(2)

if( color_green > color_red):pun.Control('COM4',buarate,speed).gotoJoint(90,5,-55,-90,45)
if( color_green < color_red):pun.Control('COM4',buarate,speed).gotoJoint(-90,5,-55,-90,45)
time.sleep(2)
pun.Control('COM4',buarate,speed).Graper(15)
time.sleep(2)
pun.Control('COM4',buarate,speed).setReady()
time.sleep(1)
pun.Control('COM4',buarate,speed).gotoHome()
time.sleep(1)
'''
pun.Control('COM4',buarate,speed).gotoHome()
objects = chang.getImage()
number_objects = len(objects)
print(number_objects)
coordinate = []
COLOR_s =  []
size = 5
f_grap = 0.4405*(size**2) + (1.775*size) - 42.06

for i in range(number_objects):

    positions_x = objects[i][1]
    positions_y = objects[i][0]
    color = objects[i][2]  
    x = ( positions_x / 10 )+10
    y = (( positions_y *-1) /10 ) +25.6

    z = 3
    y=y-5

    x = Arm.fw_kinemtic(x,y,z).findPositions()
    coordinate.append((x))
    COLOR_s.append(color)
    

print(coordinate)
print(COLOR_s)



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